"""imagersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .views import AlbumView, AlbumEditView, AlbumFormView, \
    PhotoView, PhotoEditView, PhotoFormView

"""urls begin with /images/"""
urlpatterns = [
    # url(
    #     r'^$',
    #     login_required(
    #         TemplateView.as_view(template_name='library.html')
    #     ),
    #     name='library'
    # ),

    url(
        r'^library/$',
        login_required(
            TemplateView.as_view(template_name='library.html')
        ),
        name='library'
    ),

    url(
        r'^album/(?P<pk>\d+)/$',
        login_required(
            AlbumView.as_view()
        ),
        name='album'
    ),

    url(
        r'^photos/(?P<pk>\d+)/$',
        login_required(
            PhotoView.as_view()
        ),
        name='photo'
    ),

    url(
        r'^photos/add',
        login_required(
            PhotoFormView.as_view()
        ),
        name='add_photo'
    ),

    url(
        r'^photos/edit/(?P<pk>\d+)/$',
        login_required(
            PhotoEditView.as_view()
        ),
        name='edit_photo'
    ),


    url(
        r'^album/add',
        login_required(
            AlbumFormView.as_view()
        ),
        name='add_album'
    ),

    url(
        r'^album/edit/(?P<pk>\d+)/$',
        login_required(
            AlbumEditView.as_view()
        ),
        name='edit_album'
    ),
]
