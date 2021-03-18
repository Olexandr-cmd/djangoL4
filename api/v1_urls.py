from django.urls import path, include

urlpatterns = [
    path('company/', include('company.urls')),
    path('employee/', include('employee.urls')),
    path('users/', include('users.urls'))
]