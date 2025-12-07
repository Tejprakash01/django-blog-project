from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from blog.models import Post
from .serializers import PostSerializer

class PostListAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
