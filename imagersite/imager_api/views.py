from rest_framework import viewsets
from imager_images.models import Photo
from serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        user_photos = super(PhotoViewSet, self).get_queryset()
        user_photos = user_photos.filter(user=self.request.user)
        return user_photos
