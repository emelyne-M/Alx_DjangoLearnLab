from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Setup user groups and permissions'

    def handle(self, *args, **options):
        Book = apps.get_model('bookshelf', 'Book')
        
        # Create permissions if they don't exist
        perms = ['can_view', 'can_create', 'can_edit', 'can_delete']
        for perm in perms:
            Permission.objects.get_or_create(codename=perm, name=f'Can {perm} book', content_type=Book._meta.get_field('id').model._meta)

        # Create groups
        groups = {
            'Editors': ['can_edit', 'can_create'],
            'Viewers': ['can_view'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for group_name, perm_list in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_name in perm_list:
                perm = Permission.objects.get(codename=perm_name)
                group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Groups and permissions set up successfully!'))
