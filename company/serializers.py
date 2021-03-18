from rest_framework.serializers import ModelSerializer

from company.models import CompanyModels

from employee.serializers import EmployeeSerializer


class CompanySerializer(ModelSerializer):
    employee = EmployeeSerializer(many=True, required=False)

    class Meta:
        model = CompanyModels
        exclude = ['user']
