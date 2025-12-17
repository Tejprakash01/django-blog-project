from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ChatRequest, ChatRoom, Message
from django.db.models import Q, Count
from django.db import models



@login_required
def search_users(request):
    query = request.GET.get("q", "")
    users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
    return render(request, "chat/search.html", {"users": users, "query": query})

@login_required
def send_chat_request(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    ChatRequest.objects.get_or_create(sender=request.user, receiver=receiver)
    return redirect("chat_search")

@login_required
def approve_request(request, request_id):
    chat_request = get_object_or_404(ChatRequest, id=request_id)

    # Only receiver can approve
    if chat_request.receiver != request.user:
        return redirect('chat_inbox')

    # Create chat room with BOTH users
    ChatRoom.objects.create(
        user1=chat_request.sender,
        user2=chat_request.receiver
    )

    # Mark request as approved
    chat_request.is_approved = True
    chat_request.save()

    return redirect('chat_inbox')


@login_required
def reject_request(request, req_id):
    chat_req = get_object_or_404(ChatRequest, id=req_id, receiver=request.user)
    chat_req.delete()
    return redirect("chat_inbox")



@login_required
def chat_inbox(request):
    requests = ChatRequest.objects.filter(
        receiver=request.user,
        is_approved=False
    )

    rooms = ChatRoom.objects.filter(
        Q(user1=request.user) | Q(user2=request.user)
    ).annotate(
        unread_count=Count(
            "message",
            filter=Q(message__is_read=False) & ~Q(message__sender=request.user)
        )
    ).distinct()

    return render(request, 'chat/inbox.html', {
        'requests': requests,
        'rooms': rooms
    })


@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    Message.objects.filter(room=room,is_read=False).exclude(sender=request.user).update(is_read=True)


    return render(request, 'chat/room.html', {
        'room': room,
        'messages': messages
    })
