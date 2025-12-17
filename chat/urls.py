from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search_users, name="chat_search"),
    path("send/<int:user_id>/", views.send_chat_request, name="send_chat_request"),
    path('approve/<int:request_id>/', views.approve_request, name='approve_request'),
    path("reject/<int:req_id>/", views.reject_request, name="reject_request"),
    path("inbox/", views.chat_inbox, name="chat_inbox"),
    path("room/<int:room_id>/", views.chat_room, name="chat_room"),
]
