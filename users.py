from django.contrib.auth.models import User, Group

def create_user(_username = 'username', _password = 'password'):
    user = User.objects.create_user(username=_username, password=_password)
    group = Group.objects.get(name='MyGroup')
    user.groups.add(group)