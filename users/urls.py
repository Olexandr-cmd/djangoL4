from django.urls import path

from users.views import UserListCreateView, ReadUpdateDeleteView, CompanyCreate

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('<int:pk>/', ReadUpdateDeleteView.as_view(), name='ussr_update_delete'),
    path('<int:pk>/company/', CompanyCreate.as_view(), name='company_create')
]
