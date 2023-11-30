from rest_framework import serializers

from movies.models import Genre, Certification, Director, Star, MovieStar, MovieDirector, MovieGenre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = "__all__"

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"

class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = "__all__"


class MovieDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDirector
        fields = "__all__"



class MovieStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieStar
        fields = "__all__"
