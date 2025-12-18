from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Count

from .models import ChatRequest, ChatRoom, Message


@login_required
def search_users(request):
    query = request.GET.get("q", "")
    users = (
        User.objects
        .filter(username__icontains=query)
        .exclude(id=request.user.id)
    )
    return render(request, "chat/search.html", {
        "users": users,
        "query": query
    })


@login_required
def send_chat_request(request, user_id):
    receiver = get_object_or_404(User, id=user_id)

    # 1. Prevent self request
    if receiver == request.user:
        return redirect("chat_search")

    # 2. If room already exists → no request needed
    if ChatRoom.objects.filter(
        user1__in=[request.user, receiver],
        user2__in=[request.user, receiver]
    ).exists():
        return redirect("chat_search")

    # 3. Prevent duplicate request (handled by unique constraint too)
    ChatRequest.objects.get_or_create(
        sender=request.user,
        receiver=receiver
    )

    return redirect("chat_search")


@login_required
def approve_request(request, request_id):
    chat_request = get_object_or_404(ChatRequest, id=request_id)

    # Only receiver can approve
    if chat_request.receiver != request.user:
        return redirect("chat_inbox")

    sender = chat_request.sender
    receiver = chat_request.receiver

    # Ensure consistent ordering
    user1, user2 = sorted([sender, receiver], key=lambda u: u.id)

    ChatRoom.objects.get_or_create(
        user1=user1,
        user2=user2
    )

    chat_request.is_approved = True
    chat_request.save(update_fields=["is_approved"])

    return redirect("chat_inbox")


@login_required
def reject_request(request, req_id):
    chat_req = get_object_or_404(
        ChatRequest,
        id=req_id,
        receiver=request.user
    )
    chat_req.delete()
    return redirect("chat_inbox")


@login_required
def chat_inbox(request):
    requests = ChatRequest.objects.filter(
        receiver=request.user,
        is_approved=False
    )

    rooms = (
        ChatRoom.objects
        .filter(Q(user1=request.user) | Q(user2=request.user))
        .annotate(
            unread_count=Count(
                "messages",
                filter=Q(messages__is_read=False)
                & ~Q(messages__sender=request.user)
            )
        )
        .distinct()
    )

    return render(request, "chat/inbox.html", {
        "requests": requests,
        "rooms": rooms,
    })


@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)

    messages = (
        Message.objects
        .filter(room=room)
        .order_by("timestamp")
    )

    # Mark unread messages as read (except sender)
    Message.objects.filter(
        room=room,
        is_read=False
    ).exclude(
        sender=request.user
    ).update(is_read=True)

    return render(request, "chat/room.html", {
        "room": room,
        "messages": messages
    })

@login_required
def delete_chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)

    if request.user not in [room.user1, room.user2]:
        return redirect("chat_inbox")

    # Delete messages first
    Message.objects.filter(room=room).delete()

    # Delete room
    room.delete()

    # Clean old requests
    ChatRequest.objects.filter(
        Q(sender=request.user, receiver=room.other_user(request.user)) |
        Q(sender=room.other_user(request.user), receiver=request.user)
    ).delete()

    return redirect("chat_inbox")
