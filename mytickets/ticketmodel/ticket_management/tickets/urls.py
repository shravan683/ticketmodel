from django.urls import path
from .views import create_ticket, update_ticket

urlpatterns = [
    path('create/', create_ticket, name='create-ticket'),
    path('update/<int:pk>/', update_ticket, name='update-ticket'),
]
