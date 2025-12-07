from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "title", "content", "image", "author", "created_at", "updated_at"]
