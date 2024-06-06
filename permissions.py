from django.contrib.auth.models import Permission

def create_permissions():
    Permission.objects.create(codename='can_view_user', name='Can view user', content_type__app_label='auth', content_type__model='user')
    Permission.objects.create(codename='can_add_user', name='Can add user', content_type__app_label='auth', content_type__model='user')
    Permission.objects.create(codename='can_change_user', name='Can change user', content_type__app_label='auth', content_type__model='user')
    Permission.objects.create(codename='can_delete_user', name='Can delete user', content_type__app_label='auth', content_type__model='user')