from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (CustomLoginView, CustomRegisterView, MyBookingsListView,
                    )

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        CustomLoginView.as_view(template_name=f'{app_name}/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name=f'{app_name}/logout.html'),
        name='logout'
    ),
    path(
        'register/',
        CustomRegisterView.as_view(),
        name='register'
    ),
    path(
        'me/cabinet/',
        MyBookingsListView.as_view(),
        name='cabinet'
    ),
]
