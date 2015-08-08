from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Album, Photo


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


class PhotoFormView(CreateView):
    template_name = 'photoform.html'
    model = Photo
    fields = ['title', 'description', 'image']
    success_url = '/images/library'

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        return super(PhotoFormView, self).form_valid(form)


class PhotoEditView(UpdateView):
    template_name = 'photoupdateform.html'
    model = Photo
    fields = ['title', 'description']
    success_url = '/images/library'


class AlbumFormView(CreateView):
    template_name = 'albumform.html'
    fields = ['title', 'description', 'photos', 'cover', 'published']
    model = Album
    success_url = '/images/library'

    def get_form(self):
        form = super(AlbumFormView, self).get_form()
        form.fields['photos'].queryset = self.request.user.photo_set.all()
        form.fields['cover'].queryset = self.request.user.photo_set.all()
        return form

    def form_valid(self, form):
        album = form.save(commit=False)
        album.user = self.request.user
        album.save()
        form.save_m2m()
        return super(AlbumFormView, self).form_valid(form)


class AlbumEditView(UpdateView):
    template_name = 'albumupdateform.html'
    fields = ['title', 'description', 'photos', 'cover', 'published']
    model = Album
    success_url = '/images/library'

    def get_form(self):
        form = super(AlbumEditView, self).get_form()
        form.fields['photos'].queryset = self.request.user.photo_set.all()
        form.fields['cover'].queryset = self.request.user.photo_set.all()
        return form
