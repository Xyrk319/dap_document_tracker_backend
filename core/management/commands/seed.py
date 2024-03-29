from django.core.management.base import BaseCommand
# Adjust the import paths according to your project structure
from core.seeders.RoleSeeder import seed_roles
from core.seeders.UserSeeder import seed_users
from core.seeders.PermissionSeeder import seed_permissions

class Command(BaseCommand):
    help = 'Runs all seeders.'

    def handle(self, *args, **options):
        # Call each seeder function
        seed_roles()
        seed_users()
        # seed_permissions()
        self.stdout.write(self.style.SUCCESS('Successfully ran all seeders.'))
