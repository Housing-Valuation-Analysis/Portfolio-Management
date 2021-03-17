"""Routing module"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("delete/<stock_id>", views.delete, name="delete")
]
