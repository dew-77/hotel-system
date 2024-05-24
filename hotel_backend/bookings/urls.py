from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/<slug:layout_slug>/', views.book_layout, name='book'),
    path(
        'check_availability/',
        views.check_availability, name='check_availability'
    ),
    path(
        'confirm_booking/<slug:layout_slug>/',
        views.confirm_booking, name='confirm_booking'
    ),
    path(
        'success/<int:booking_id>/',
        views.booking_presuccess, name='presuccess'
    ),
    path('pay/<int:booking_id>/', views.booking_pay, name='pay'),
    path('confirm/<int:booking_id>/', views.booking_confirm, name='confirm'),
    path(
        'precancel/<int:booking_id>/',
        views.booking_precancel, name='precancel'
    ),
    path('cancel/<int:booking_id>/', views.booking_cancel, name='cancel'),
]
