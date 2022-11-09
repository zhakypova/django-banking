from django.urls import path

from .views import IndexView, DetailClient

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('client/<int:pk>/', DetailClient.as_view(), name='detail'),
]