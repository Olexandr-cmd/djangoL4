from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

from company.models import CompanyModels


# Create your models here.

class EmployeeModel(models.Model):
    class Meta:
        db_table = 'employee'
        verbose_name = 'name'

    name = models.CharField(max_length=20, validators=[RegexValidator('^[a-zA-Z]{2,20}$')])
    surname = models.CharField(max_length=20, validators=[RegexValidator('^[a-zA-Z]{2,20}$')])
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(60)])
    profession = models.CharField(max_length=30)
    create = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(CompanyModels, on_delete=models.CASCADE, related_name='company')

