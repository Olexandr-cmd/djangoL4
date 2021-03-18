from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404

from company.serializers import CompanySerializer
from employee.serializers import EmployeeSerializer
from company.models import CompanyModels


# Create your views here.


class CompanyCreateView(ListCreateAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        qs = CompanyModels.objects.all()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__iexact=name)
        return qs


class CreateEmployee(CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        company_id = self.kwargs.get('pk')
        company = get_object_or_404(CompanyModels, pk=company_id)
        serializer.save(company=company)


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = CompanyModels.objects.all()
    serializer_class = CompanySerializer
