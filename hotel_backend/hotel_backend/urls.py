from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls', namespace='bookings')),
    path('reviews/', include('reviews.urls', namespace='rooms')),

    path('rooms/', include('rooms.urls', namespace='reviews')),
    path(
        'services/',
        include('additional_services.urls', namespace='additional_services')
    ),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
