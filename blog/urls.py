from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("create/", views.create_post, name="create_post"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path("delete/<int:post_id>/", views.delete_post, name="delete_post"),

    path("like/<int:post_id>/", views.like_post_ajax, name="like_post_ajax"),
    path("comment/add/<int:post_id>/", views.add_comment_ajax, name="add_comment"),
    path("comment/delete/<int:comment_id>/", views.delete_comment_ajax, name="delete_comment"),

    path("profile/<str:username>/", views.profile, name="profile"),
    path("register/", views.register_view, name="register"),

    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
