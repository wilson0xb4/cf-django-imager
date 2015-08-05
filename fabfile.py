# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import boto.ec2
from fabric.api import run, env, prompt, execute, sudo, local
from fabric.contrib.files import upload_template
import time

env.hosts = ['localhost']
env.aws_region = 'us-west-2'


def host_type():
    run('uname -s')


def get_ec2_connection():
    if 'ec2' not in env:
        conn = boto.ec2.connect_to_region(env.aws_region)
        if conn is not None:
            env.ec2 = conn
            print("Connected to EC2 region {}".format(env.aws_region))
        else:
            msg = "Unable to connect to EC2 region {}"
            raise IOError(msg.format(env.aws_region))
    return env.ec2


def provision_instance(wait_for_running=True, timeout=60, interval=2):
    """Create a new AWS EC2 instance for the user specified in .boto"""
    wait_val = int(interval)
    timeout_val = int(timeout)
    conn = get_ec2_connection()
    instance_type = 't2.micro'
    key_name = 'pk-aws'
    security_group = 'ssh-access'
    image_id = 'ami-5189a661'

    reservations = conn.run_instances(
        image_id,
        key_name=key_name,
        instance_type=instance_type,
        security_groups=[security_group]
    )
    new_instances = [i for i in reservations.instances if i.state == 'pending']
    running_instance = []
    if wait_for_running:
        waited = 0
        while new_instances and (waited < timeout_val):
            time.sleep(wait_val)
            # waited += wait_val  # is this importan?
            for instance in new_instances[:]:  # copy list so we aren't mutating a list as we are iterating it
                state = instance.state
                print("Instance {} is {}".format(instance.id, state))
                if state == "running":
                    running_instance.append(
                        new_instances.pop(new_instances.index(i))
                    )
                instance.update()


def stop_running_instance():
    select_instance()
    print(env.active_instance.state)
    env.active_instance.stop()
    env.active_instance.update()
    print(env.active_instance.state)


def terminate_stopped_instance():
    select_instance(state='stopped')
    print(env.active_instance.state)
    env.active_instance.terminate()
    print(env.active_instance.state)


def list_aws_instances(verbose=False, state='all'):
    """Returns a list of EC2 instances for the user specified in .boto"""
    conn = get_ec2_connection()

    reservations = conn.get_all_reservations()
    instances = []
    for res in reservations:
        for instance in res.instances:
            if state == 'all' or instance.state == state:
                instance = {
                    'id': instance.id,
                    'type': instance.instance_type,
                    'image': instance.image_id,
                    'state': instance.state,
                    'instance': instance
                }
                instances.append(instance)
    env.instances = instances
    if verbose:
        import pprint
        pprint.pprint(env.instances)


def select_instance(state='running'):
    """Allow user to choose which instance to work on."""
    if env.get('active_instance', False):
        return

    list_aws_instances(state=state)

    prompt_text = "Please select from the following instances:\n"
    instance_template = "{ct}: {state} instance {id}\n"
    for idx, instance in enumerate(env.instances):
        ct = idx + 1
        args = {'ct': ct}
        args.update(instance)
        prompt_text += instance_template.format(**args)
    prompt_text += "Coose an isntance: "

    def validation(input):
        choice = int(input)
        if choice not in range(1, len(env.instances) + 1):
            raise ValueError("{} is not a valid instance".format(choice))
        return choice

    choice = prompt(prompt_text, validate=validation)
    env.active_instance = env.instances[choice - 1]['instance']


def run_command_on_targeted_server(command):
    """Run a command while targeting a selected EC2 instance.
    In most cases, the command is run on the targeted server.
    """
    select_instance()
    selected_hosts = [
        'ubuntu@' + env.active_instance.public_dns_name
    ]
    execute(command, hosts=selected_hosts)


def _ssh_deploy_key():
    server_name = env.active_instance.public_dns_name
    local("scp -o StrictHostKeyChecking=no id_rsa ubuntu@" + server_name + ":~/.ssh/")
    local("scp -o StrictHostKeyChecking=no id_rsa.pub ubuntu@" + server_name + ":~/.ssh/")
    sudo('eval "$(ssh-agent -s)"; ssh-add ~/.ssh/id_rsa')
    sudo('chmod 400 ~/.ssh/id_rsa')


def ssh_deploy_key():
    """Copy public and private keys to server, start ssh-agent,
    adjust key permissions.

    Assumes id_rsa is in the same directory as the fabfile.
    """
    run_command_on_targeted_server(_ssh_deploy_key)


def _install_nginx():
    sudo('apt-get -y install nginx')

    server_name = env.active_instance.public_dns_name

    upload_template(
        filename='simple_nginx_config_template',
        destination='/etc/nginx/sites-available/default',
        context={'address': server_name},
        use_sudo=True,
        backup=True
    )

    sudo('service nginx restart')


def install_nginx():
    """Install nginx, move conf files into place, start service.

    Assumes simple_nginx_config_template is in the same directory as
    the fabfile.
    """
    run_command_on_targeted_server(_install_nginx)


def _apt_get_update():
    sudo('apt-get -y update')


def apt_get_update():
    """When an EC2 instance isn't updated...."""
    run_command_on_targeted_server(_apt_get_update)


def _install_git():
    sudo('apt-get -y install git')


def install_git():
    """git doesn't come by default?"""
    run_command_on_targeted_server(_install_git)


def _install_pip():
    sudo('apt-get -y install python-pip')


def install_pip():
    """pip doesn't come by default?"""
    run_command_on_targeted_server(_install_pip)


def _pip_update():
    sudo('pip install -r ~/django-imager/requirements.txt')


def pip_update():
    """Install all from requirements file."""
    run_command_on_targeted_server(_pip_update)


def _git_clone():
    """ssh-keyscan adds github so we don't get asked to accept fingerprint"""
    run('ssh-keyscan github.com >> ~/.ssh/known_hosts')
    run("git clone git@github.com:wilson0xb4/django-imager.git ~/django-imager")


def git_clone():
    """Initial clone from git repo."""
    run_command_on_targeted_server(_git_clone)


def _move_files():
    """pulling from staging for dev, switch to master for production"""
    run("cd ~/django-imager; git pull origin master")


def move_files():
    """Update files from git repo"""
    run_command_on_targeted_server(_move_files)


def _update_nginx_config():
    server_name = env.active_instance.public_dns_name
    upload_template(
        filename='simple_nginx_config_template',
        destination='/etc/nginx/sites-available/default',
        context={'address': server_name},
        use_sudo=True,
        backup=True
    )
    sudo('service nginx restart')


def update_nginx_config():
    """Copy new nginx config file, move it into place, restart server.

    Update function was added when we ran into CORS issue and needed to
    update the nginx config across both servers.
    """
    run_command_on_targeted_server(_update_nginx_config)


def initial_deploy():
    """after a server has been provisioned, this will full setup a
    server for the django-imager project.

    Assumes supervisord.conf, simple_nginx_config_template, and id_rsa
    are in the same directory as the fabfile.
    """
    ssh_deploy_key()
    apt_get_update()
    install_pip()
    install_git()
    git_clone()
    pip_update()
    install_nginx()


def deploy():
    """sync files, check requirements file, and restart supervisor"""
    move_files()
    pip_update()
