from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

SHIRT_SIZES = [
    ('xs', 'xs'),
    ('s', 's'),
    ('m', 'm'),
    ('l', 'l'),
    ('xl', 'xl'),
    ('2xl', '2xl'),
    ('3xl', '3xl'),
]


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        """
        Create and return a `User` with an email, phone number username and password
        :param username:
        :param email:
        :param password:
        :param kwargs:
        :return:
        """
        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permission
        :param username:
        :param email:
        :param password:
        :return:
        """
        if password is None:
            raise TypeError('Superusers must have a password')
        if email is None:
            raise TypeError('Superusers must have an email')
        if username is None:
            raise TypeError('Superusers must have a username')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(blank=True, auto_created=True, auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True, auto_now=True)

    # Non required Fields
    nickname = models.CharField(max_length=23, blank=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    shift_info_email = models.BooleanField(default=True, help_text='User wants to be informed via email about shifts')
    shirt_size = models.CharField(max_length=3, choices=SHIRT_SIZES, default=None, blank=True, null=True)
    arrived = models.BooleanField(default=False)
    arrival = models.DateField(blank=True, null=True)
    planned_arrival = models.DateField(blank=True, null=True)
    planned_departure = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
