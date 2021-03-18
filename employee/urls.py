from django.urls import path

from employee.views import EmployeeCreateView, ReadUpdateDeleteView

urlpatterns = [
    path('', EmployeeCreateView.as_view(), name='employee_create'),
    path('<int:pk>/', ReadUpdateDeleteView.as_view(), name='employee_create_delete')
]