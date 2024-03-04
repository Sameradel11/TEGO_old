from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, User
# Create your views here.




class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    mobile_number = models.CharField(max_length=15)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    commercial_registration_number = models.CharField(max_length=255)
    tax_card_number = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    landline = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255)
    company_type = models.CharField(max_length=255)
    company_capital= models.IntegerField()
    def __str__(self):
        return self.name
    
    @property
    def owners(self):
        return self.owner_set.all()


class Owner(models.Model):
    name = models.CharField(max_length=100)
    owner_id = models.CharField(max_length=20)
    onwer_position=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Branche(models.Model):
    address=models.TextField()
    city=models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.city

class CompanyField(models.Model):
    primary_field=models.CharField(max_length=255)
    secondary_field=models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.primary_field
