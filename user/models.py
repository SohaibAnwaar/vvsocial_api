from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.postgres.fields import JSONField
from django.conf import settings

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "sohaibanwaar1203@gmail.com",
        # to:
        [reset_password_token.user.email],
         fail_silently=False,
         auth_password="AsB_R6566",
         auth_user="sohaibanwaar1203@gmail.com"
    )



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)
#     about_user = JSONField(null=True, blank=True)

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         super().save(force_insert, force_update, using, update_fields)

#         img = Image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)


# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone



class Profile(models.Model):

    GENRE_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    MARITAL_STATUS_CHOICES = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('d', 'Divorsed'),
        ('C', 'Complecated'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES,null=True)
    address = models.CharField(max_length=150,null=True)
    postal_code_4 = models.PositiveIntegerField(null=True)
    postal_code_3 = models.PositiveIntegerField(null=True)
    locatity = models.CharField(max_length=30,null=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES,null=True)
    child_amount = models.PositiveSmallIntegerField(null=True)
    about_user = JSONField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)


    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        
# User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])