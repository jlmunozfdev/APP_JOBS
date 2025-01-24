from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/job/<int:pk>/', views.job_detail, name='job_detail'),
    path('add/', views.job_create, name='job_create'),
    path('edit/<int:pk>/', views.job_update, name='job_update'),
    path('delete/<int:pk>/', views.job_delete, name='job_delete'),
]


