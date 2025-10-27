from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    # Компании
    path('companies/', views.company_list, name='company_list'),
    path('companies/add/', views.company_create, name='company_add'),
    path('companies/<int:pk>/edit/', views.company_edit, name='company_edit'),
    path('companies/<int:pk>/delete/', views.company_delete, name='company_delete'),

    # Клиенты
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.client_create, name='client_add'),
    path('clients/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),

    path('login/', auth_views.LoginView.as_view(template_name='crm/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
