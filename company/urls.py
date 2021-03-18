from django.urls import path

from company.views import CompanyCreateView, ReadUpdateDeleteView, CreateEmployee

urlpatterns = [
    path('', CompanyCreateView.as_view(), name='cars_create'),
    path('<int:pk>/', ReadUpdateDeleteView.as_view(), name='cars_update_delete'),
    path('<int:pk>/employee/', CreateEmployee.as_view(), name='create_employee')
]
