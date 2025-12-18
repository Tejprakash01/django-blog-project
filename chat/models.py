from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ChatRequest(models.Model):
    sender = models.ForeignKey(
        User,
        related_name="sent_requests",
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        related_name="received_requests",
        on_delete=models.CASCADE
    )
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["sender", "receiver"],
                name="unique_chat_request"
            )
        ]

    def __str__(self):
        return f"{self.sender} → {self.receiver}"


class ChatRoom(models.Model):
    user1 = models.ForeignKey(
        User,
        related_name="chat_rooms_as_user1",
        on_delete=models.CASCADE
    )
    user2 = models.ForeignKey(
        User,
        related_name="chat_rooms_as_user2",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user1", "user2"],
                name="unique_chat_room"
            )
        ]

    def save(self, *args, **kwargs):
        # Always store users in consistent order to prevent duplicates
        if self.user1_id and self.user2_id and self.user1_id > self.user2_id:
            self.user1, self.user2 = self.user2, self.user1
        super().save(*args, **kwargs)

    def other_user(self, user):
        return self.user2 if user == self.user1 else self.user1

    def __str__(self):
        return f"Chat: {self.user1} & {self.user2}"


class Message(models.Model):
    room = models.ForeignKey(
        ChatRoom,
        related_name="messages",
        on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        User,
        related_name="sent_messages",
        on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender}: {self.content[:30]}"
