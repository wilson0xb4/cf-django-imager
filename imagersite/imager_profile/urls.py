from django.conf.urls import url
from imager_profile.views import ImagerProfileList


urlpatterns = [
    url(r'^$', ImagerProfileList.as_view()),
]
