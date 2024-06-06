from django.shortcuts import redirect

def base_home(request):
    return redirect('chat')
