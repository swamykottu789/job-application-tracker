from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('add/', views.add_job, name='add_job'),

    path('edit/<int:id>/', views.edit_job, name='edit_job'),

    path('delete/<int:id>/', views.delete_job, name='delete_job'),

]