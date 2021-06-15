from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username="", password=""):

#         print(username)
#         """
#         Creates and saves a User with the given email and password.

#         NOTE: Argument 'username' is needed for social-auth. It is not actually used.
#         """
#         if not email:
#             raise ValueError('Email harus dengan format email yang benar.')

#         # Validate email is unique in database
#         if Account.objects.filter(email = self.normalize_email(email).lower()).exists():
#             raise ValueError('email sudah teregistrasi.')

#         user = self.model(
#             email=self.normalize_email(email).lower(),
#         )

#         user.set_password(password)

#         # Save and catch IntegrityError (due to email being unique)
#         try:
#             user.save(using=self._db)

#         except IntegrityError:
#             raise ValueError('This email has already been registered.')

#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
        
# class Account(AbstractBaseUser):

#     objects = MyAccountManager()

#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#         error_messages={
#             'unique':"This email has already been registered.",
#         }
#     )

#     # Custom: was this email validated, at some point, by sending an email?
#     # is_email_validated = models.BooleanField(default=False)

#     # email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username                = models.CharField(max_length=30, unique=True)
#     date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin                = models.BooleanField(default=False)
#     is_active               = models.BooleanField(default=True)
#     is_staff                = models.BooleanField(default=False)
#     is_superuser            = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = ['email','username','password']
    
#     USERNAME_FIELD = 'email'

#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email

#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email

#     def __str__(self):
#         return self.email

#     def __unicode__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

# class myaccount(models.Model):
#   client_name = models.CharField(max_length=500, null=True,blank=True)
#   product_name = models.CharField(max_length=500, null=True,blank=True)
#   amount = models.FloatField(max_length=500, null=True,blank=True)
#   price = models.FloatField(max_length=500, null=True,blank=True)
#   comment = models.CharField(max_length=500, null=True,blank=True)
#   created = models.DateTimeField(auto_now_add=True)
  
#   def __str__(self):
#     suser = '{0.client_name} {0.product_name}'
#     return suser.format(self)

# Create your models here.
class Conversation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=225)
    message = models.CharField(blank=True, null=True, max_length=225)
    status = models.CharField(blank=True, null=True, max_length=225)
    created_at = models.DateTimeField(auto_now=True)