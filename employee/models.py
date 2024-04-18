from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.conf import settings




class CustomUser(AbstractUser):
    id = models.IntegerField(primary_key=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_country_code = models.CharField(max_length=5, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    class Meta:
        db_table = 'custom_user'





class Notification(models.Model):
    pass
