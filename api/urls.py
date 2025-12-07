from django.urls import path
from .views import PostListCreateAPI, PostDetailAPI

urlpatterns = [
    path("posts/", PostListCreateAPI.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetailAPI.as_view(), name="api_post_detail"),
]
