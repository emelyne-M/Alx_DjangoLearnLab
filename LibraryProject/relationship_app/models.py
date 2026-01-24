from django.db import models
from django.contrib.auth.models import User,AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

user = models.OneToOneField(
    settings.AUTH_USER_MODEL,  # use custom user model
    on_delete=models.CASCADE
)




class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return self.name
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,  
    on_delete=models.CASCADE
)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# Signal to automatically create UserProfile when a new user is registered
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
       
class Meta:
    permissions = [
        ("can_add_book", "Can add book"),
        ("can_change_book", "Can change book"),
        ("can_delete_book", "Can delete book"),
    ]


# Custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Username is required")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, password, **extra_fields)

# Custom user model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.username
