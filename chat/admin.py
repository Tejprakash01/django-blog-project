from django.contrib import admin
from .models import ChatRequest, ChatRoom, Message


@admin.register(ChatRequest)
class ChatRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('sender__username', 'receiver__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'user1', 'user2', 'created_at')
    search_fields = ('user1__username', 'user2__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'sender', 'is_read', 'timestamp')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('content', 'sender__username')
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp',)
