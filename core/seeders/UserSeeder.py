from django.contrib.auth.hashers import make_password
from api_auth.models import User, Role

def seed_users():
    # Ensure the roles exist
    admin_role, _ = Role.objects.get_or_create(name='Admin')
    user_role, _ = Role.objects.get_or_create(name='User')
    
    users_data = [
        {"email": "admin@example.com", "password": "adminpass", "role": admin_role},
        {"email": "user@example.com", "password": "userpass", "role": user_role},
    ]

    for user_data in users_data:
        user, created = User.objects.get_or_create(email=user_data['email'], defaults={
            'password': make_password(user_data['password']),  # Hash the password
            'role': user_data['role'],
        })
        if created:
            print(f'User {user.email} created.')
        else:
            print(f'User {user.email} already exists.')
