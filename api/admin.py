from django.contrib import admin
from .models import CustomUser,Company,Owner
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(Owner)
