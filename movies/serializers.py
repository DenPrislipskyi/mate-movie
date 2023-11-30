from rest_framework import serializers

from movies.models import Genre, Certification, Director, Star, MovieStar, MovieDirector, MovieGenre, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
