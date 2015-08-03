from django.views.generic import TemplateView
from imager_images.models import Album, Photo


class AlbumView(TemplateView):
    template_name = 'album.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)

        try:
            context['user'] = self.request.user
            album_set = self.request.user.album_set
            context['album'] = album_set.get(id=kwargs.get('pk'))
        except Album.DoesNotExist:
            pass

        return context


class PhotoView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)

        try:
            context['user'] = self.request.user
            photo_set = self.request.user.photo_set
            context['photo'] = photo_set.get(id=kwargs.get('pk'))
        except Photo.DoesNotExist:
            pass

        return context
