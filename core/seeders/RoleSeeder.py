from api_auth.models import Role
from api_auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def seed_roles():
    roles = ['Admin', 'User']
    for role_name in roles:
        role, created = Role.objects.get_or_create(name=role_name)
        if created:
            print(f'Role {role_name} created.')
        else:
            print(f'Role {role_name} already exists.')
    

    admin_role, created = Role.objects.get_or_create(name='Admin')
    models = [User, Permission]
    for model in models:
        # Get the ContentType for the current model
        content_type = ContentType.objects.get_for_model(model)
        
        # Fetch all permissions associated with the model
        permissions = Permission.objects.filter(content_type=content_type)
        
        # Assign the fetched permissions to the 'Admin' role
        for permission in permissions:
            admin_role.permissions.add(permission)