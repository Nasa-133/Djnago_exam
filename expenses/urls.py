from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('expense/create/', views.expense_create, name='expense_create'),
    path('expense/<int:pk>/edit/', views.expense_edit, name='expense_edit'),
    path('expense/<int:pk>/delete/', views.expense_delete, name='expense_delete'),

]