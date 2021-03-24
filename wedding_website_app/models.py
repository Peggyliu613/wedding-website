from django.db import models
from django.contrib.auth.models import User
import re
import bcrypt

DIET_CHOICE = (
    ('none', 'none'),
    ('vegan', 'vegan'),
    ('vegetarian', 'vegetarian'),
    ('other', 'other'),
)
class GuestManager(models.Manager):
    def validator(self, postdata, is_shu_friend_relative, is_peggy_friend_relative):
        errors={}
        is_email_used=Guest.objects.filter(email=postdata['email'])
        if len(is_email_used)>0:
            errors['email']="Your email is used"
        if len(postdata['full_name'])<2:
            errors['full_name']="Your name should be at least 2 characters"
        if not re.search(".+@.+\..+", postdata['email']):
            errors['email']="Your email is invalid"
        if not is_shu_friend_relative and not is_peggy_friend_relative:
            errors['friendship']="Pick Shu-Hao or Peggy"
        return errors

class Guest(models.Model):
    full_name=models.CharField(max_length=64)
    email=models.CharField(max_length=64)
    is_shu_friend_relative = models.BooleanField(default=False)
    is_peggy_friend_relative = models.BooleanField(default=False)
    number_of_guests=models.IntegerField()
    diet_restriction = models.CharField(max_length=10, choices=DIET_CHOICE, default='none')
    diet_message = models.CharField(max_length=128, null=True)
    message=models.TextField(max_length=2048, null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    objects=GuestManager()

    def __str__(self):
        return self.full_name
