from django.urls import path
from .views import PostListCreateAPI, PostDetailAPI, like_post_api

urlpatterns = [
    path("posts/", PostListCreateAPI.as_view()),
    path("posts/<int:pk>/", PostDetailAPI.as_view()),
    path("like/<int:post_id>/", like_post_api),
]
