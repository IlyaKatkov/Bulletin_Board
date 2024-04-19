from rest_framework import serializers

from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Comment
        fields = ('text', 'ad', 'created_at',)


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели

    class Meta:
        model = Ad
        fields = ('title', 'price', 'description', 'created_at',)

