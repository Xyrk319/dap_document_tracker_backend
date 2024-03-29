from api_auth.models import Role

def seed_roles():
    roles = ['Admin', 'User']
    for role_name in roles:
        role, created = Role.objects.get_or_create(name=role_name)
        if created:
            print(f'Role {role_name} created.')
        else:
            print(f'Role {role_name} already exists.')
