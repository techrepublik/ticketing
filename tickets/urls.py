from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),

    # Dashboard
    path('', views.dashboard_view, name='dashboard'),

    # Ticket URLs
    path('tickets/', views.ticket_list_view, name='ticket-list'),
    path('tickets/create/', views.ticket_create_view, name='ticket-create'),
    path('tickets/<int:pk>/update/',
         views.ticket_update_view, name='ticket-update'),
    path('tickets/<int:pk>/delete/',
         views.ticket_delete_view, name='ticket-delete'),

    # Category URLs
    path('categories/', views.category_list_view, name='category-list'),
    path('categories/create/', views.category_create_view, name='category-create'),
    path('categories/<int:pk>/update/',
         views.category_update_view, name='category-update'),
    path('categories/<int:pk>/delete/',
         views.category_delete_view, name='category-delete'),
]
