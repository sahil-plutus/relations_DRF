from rest_framework import serializers
from .models import Singer, Song


class SingerSerializer(serializers.ModelSerializer):
    # return a link for object detail
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="song-detail")

    # return a strine of object acording model str method
    # song = serializers.StringRelatedField(many=True)

    # return a primary key(id) of object
    song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


