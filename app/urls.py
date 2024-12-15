# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('transactions/', views.TransactionListView.as_view(), name='transaction-list'),
]

