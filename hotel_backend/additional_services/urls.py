from django.urls import path
from . import views

app_name = 'additional_services'

urlpatterns = [
    path('list/', views.ServiceListView.as_view(), name='list'),
    path('submit/', views.submit_services, name='submit_services'),
]
