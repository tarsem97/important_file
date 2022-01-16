from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager



class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=250)
    email = models.EmailField(_('email address'), unique=True)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250, null=True, blank=True)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=40)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class Message(models.Model):
    send_id = models.TextField(blank=True, null=True)
    success = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(null=False, auto_now_add=True)
    end_date = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        db_table = 'messages'


class Response_message(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='upload_main/')

    class Meta:
        db_table = 'response_message'

# Create your models here.
