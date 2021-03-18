from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.

class CompanyModels(models.Model):
    class Meta:
        db_table = 'company'
        verbose_name = 'name'

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='company')

