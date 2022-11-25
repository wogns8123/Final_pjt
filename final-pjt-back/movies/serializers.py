from rest_framework import serializers

from movies.models import Comment, Genre, Movie


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'released_date', 'vote_count', 'vote_average', 'overview', 'poster_path', 'genres', 'like_users', 'get_id', 'backdrop_path', 'comment_set',)


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'username')


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


class GenreMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id',)


class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)


    class Meta:
        model = Movie
        fields = ('id', 'title',)


class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class GenreMovieSerializer(serializers.ModelSerializer):
    genre_movies = MovieGenreSerializer(many=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'genre_movies')


class MovieUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fileds = ('id', 'like_users')