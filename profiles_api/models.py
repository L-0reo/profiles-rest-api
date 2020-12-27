from django.db import models
# we will want to change the authentication from a user name to user email so we import the following two django base models
from django.contrib.auth.models import AbstractBaseUser #1
from django.contrib.auth.models import PermissionsMixin #2 these two are django base models in authentication, which I'll modify when overriding the standard django user model
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):  #password=None allows for a password not to be passed
        """create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name) #by default the model here is set to the type of model that the manager is for

        user.set_password(password)
        user.save(using=self.db) #standard save into database

        return user

    def create_superuser(self, email, name, password): #this time passing in a password is mandatory
        """create and save new super user with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database odel for users in the system"""
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return  self.name

    def __str__(self):
        """return string representation of our user"""
        return self.email
