from django.shortcuts import render, redirect
from.models import Chat, ChatParticipantRole, CustomUser
#from.forms import RegistrationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserForm, NewChatForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def user_login(request):
    if request.method == 'POST':
        data=request.POST
        username = data['username']
        password = data['password']
        print(f'Username: {username}')
        print(f'Password: {password}')
        #user = UserProfileInfo.objects.get(username=username)
        #print(f'User by name: {user}')
        user = authenticate(username=username, password=password)
        print(f'User: {user}')
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')  # Success message
            return redirect('chat')
        else:
            messages.error(request, 'Invalid username or password')  # Error message
            return render(request, 'login.html', {'error': True})
    else:
        return render(request, 'login.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        #userprofile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid(): #and userprofile_form.is_valid()
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            #user_profile = userprofile_form.save(commit=False)
            #user_profile.user = user
            #if 'profile_pic' in request.FILES:
            #    user_profile.profile_pic = request.FILES['profile_pic']
            #user_profile.save()
            registered = True
            return redirect('login')  # redirect to chat page after registration
        else:
            print(user_form.errors)
            return render(request, 'register.html')
    else:
        user_form = UserForm()
        #userprofile_form = UserProfileInfoForm()

    return render(request, 'register.html')


@login_required
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('user_profile')
    return render(request, 'user_profile.html', {'user': user})

@login_required
def new_chat(request):
    """
    This view function allows a logged-in user to create a new chat.
    It renders the 'new_chat.html' template when accessed via a GET request.
    When a POST request is received, it processes the form data and creates a new chat instance.
    If the form data is valid, it creates a new ChatParticipantRole instance with the current user as the admin and adds the user as a participant.
    Finally, it redirects the user to the chat list page.
    """

    if request.method == 'POST':
        """
        Process the form data and create a new chat instance.
        """
        form = NewChatForm(request.POST)
        if form.is_valid():
            """
            If the form data is valid, create a new chat instance and a new ChatParticipantRole instance with the current user as the admin and add the user as a participant.
            """
            chat = form.save()
            chat.creator = request.user
            #
            chat_participant_role = ChatParticipantRole.objects.create(chat=chat, user=request.user, role='admin')
            #chat_participant_role.save(commit=False)
            chat.participants.add(chat_participant_role.user)
            return redirect('chat_list')  # redirect to chat list page
    else:
        """
        Render the 'new_chat.html' template with an empty form.
        """
        form = NewChatForm()
    return render(request, 'new_chat.html', {'form': form})

@login_required
def chat_list(request):
    """
    This view function displays a list of all chats that the current user is a participant of.
    It renders the 'chat_list.html' template when accessed via a GET request.
    """
    #chats = Chat.objects.filter(chatparticipantrole__user=request.user)
    chats = Chat.objects.filter(participants=request.user)
    return render(request, 'chat_list.html', {'chats': chats})

def chat_detail(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    if request.method == 'POST':
        if 'text' in request.POST:
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.user = request.user
                message.save()
                chat.messages.add(message)
                return redirect('chat_detail', pk=pk)
        elif 'username' in request.POST:
            username = request.POST['username']
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                messages.error(request, 'User does not exist')
                return redirect('chat_detail', pk=pk)
            chat.participants.add(user)
            return redirect('chat_detail', pk=pk)
    else:
        form = MessageForm()
    return render(request, 'chat_detail.html', {'chat': chat, 'form': form})
