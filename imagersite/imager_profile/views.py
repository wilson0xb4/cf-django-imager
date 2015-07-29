from django.views.generic import ListView
from imager_profile.models import ImagerProfile


class ImagerProfileList(ListView):
    model = ImagerProfile
    template_name = 'books/acme_list.html'
