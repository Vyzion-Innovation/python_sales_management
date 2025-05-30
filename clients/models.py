from django.db import models
from django.conf import settings
from common_country_module.models import Country

class Client(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=150)
    pan = models.TextField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=150)
    street_address = models.TextField()
    client_type = models.CharField(max_length=150)
    gstin = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    postal_code = models.CharField(max_length=15,)
    client_region = models.CharField(max_length=15, default = 'Unknown')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name
