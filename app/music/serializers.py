from rest_framework.serializers import ModelSerializer
from .models import Performer, Album, Song


class PerformerSerializer(ModelSerializer):
    class Meta:
        model = Performer
        fields = ('name', )


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'