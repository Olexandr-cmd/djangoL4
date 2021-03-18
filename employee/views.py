from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from employee.serializers import EmployeeSerializer
from employee.models import EmployeeModel


class EmployeeCreateView(ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        qs = EmployeeModel.objects.all()
        surname = self.request.query_params.get('surname')
        if surname:
            qs = qs.filter(surname__iexact=surname)
        return qs


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
