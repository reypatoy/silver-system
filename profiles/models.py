from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = ((1, "Admin"), (2, "Staff"), (3, "Client"))
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=1)


class AdminUser(models.Model):
    profile_pic = models.ImageField(upload_to="avatars", default="no_avatar.png")
    bio = models.TextField(default="no bio")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    auth_user_id = models.OneToOneField(
        CustomUser, related_name="adminusers", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.auth_user_id.first_name} {self.auth_user_id.last_name}"


class StaffUser(models.Model):
    profile_pic = models.ImageField(upload_to="avatars", default="no_avatar.png")
    bio = models.TextField(default="no bio")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    auth_user_id = models.OneToOneField(
        CustomUser, related_name="staffusers", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.auth_user_id.first_name} {self.auth_user_id.last_name}"


class ClientUser(models.Model):
    profile_pic = models.ImageField(upload_to="avatars", default="no_avatar.png")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    address_town = models.CharField(max_length=255, blank=True, null=True)
    address_province = models.CharField(max_length=255, blank=True, null=True)
    address_country = models.CharField(max_length=255, default="Philippines")
    address_zip_code = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(default="no bio")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    auth_user_id = models.OneToOneField(
        CustomUser, related_name="clientusers", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.auth_user_id.first_name} {self.auth_user_id.last_name}"
