from django.urls import path

from .views import MainPageView

app_name = 'homepage'

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
]
