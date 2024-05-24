from django.urls import path

from .views import RoomListView, LayoutDetailView, LayoutListView

app_name = 'rooms'

urlpatterns = [
    # path('', RoomListView.as_view(), name='room_list'),
    path('layouts/', LayoutListView.as_view(), name='layout_list'),
    path(
        'layouts/<slug:slug>/',
        LayoutDetailView.as_view(), name='layout_detail'
    ),

    # path('<int:id>', ...),
]
