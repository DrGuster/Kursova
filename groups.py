from django.contrib.auth.models import Group, Permission

def create_group():
    group = Group.objects.create(name='MyGroup')
    view_user_perm = Permission.objects.get(codename='can_view_user')
    add_user_perm = Permission.objects.get(codename='can_add_user')
    change_user_perm = Permission.objects.get(codename='can_change_user')
    delete_user_perm = Permission.objects.get(codename='can_delete_user')
    group.permissions.set([view_user_perm, add_user_perm, change_user_perm, delete_user_perm])