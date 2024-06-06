from django.shortcuts import render
from.models import Message

def chat(request):
    messages = Message.objects.all()
    return render(request, 'chat.html', {'messages': messages})
