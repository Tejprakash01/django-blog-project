from .models import ChatRequest

def chat_notifications(request):
    if request.user.is_authenticated:
        return {
            "chat_request_count": ChatRequest.objects.filter(
                receiver=request.user,
                approved=False
            ).count()
        }
    return {}
