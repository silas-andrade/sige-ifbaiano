from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O usuário precisa ter um email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None  # remove username

    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)

    objects = UserManager()  # 👈 MUITO IMPORTANTE

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'matricula']

    def __str__(self):
        return self.email

    #
    # Email: silas@i.com
    # Senha: silas123

