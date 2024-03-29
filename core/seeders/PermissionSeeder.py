from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from api_auth.models import Role, User 

def seed_permissions():
    # Define model permissions
    models_permissions = {
        'user': ['add_user', 'change_user', 'delete_user', 'view_user'],
        'role': ['add_role', 'change_role', 'delete_role', 'view_role'],
        # Add more models and their permissions as needed
    }

    # Create or get permissions
    for model, perms in models_permissions.items():
        content_type = ContentType.objects.get(app_label='api_auth', model=model)
        for codename in perms:
            name = codename.replace('_', ' ').replace('user', model).capitalize()
            perm, created = Permission.objects.get_or_create(
                codename=codename,
                name=name,
                content_type=content_type,
            )
            if created:
                print(f'Permission {name} created.')
            else:
                print(f'Permission {name} already exists.')

    # Assign permissions to roles (example: assigning all 'user' permissions to the 'Admin' role)
    admin_role, _ = Role.objects.get_or_create(name='Admin')
    user_permissions = Permission.objects.filter(content_type__model='User')
    for perm in user_permissions:
        # Assuming Role model has a ManyToMany field to Permission named 'permissions'
        admin_role.permissions.add(perm)
    print("Assigned user permissions to Admin role.")
