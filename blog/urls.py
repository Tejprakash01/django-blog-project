from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('create/', views.create_post, name='create_post'),

    # ✅ AUTH
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ✅ EXTRA
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),



]
