"""Routing module"""
from django.urls import path
from .views import home_view, about_view, dashboard_view, delete

urlpatterns = [
    path('', home_view, name="home"),
    path('about/', about_view, name="about"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("delete/<stock_id>", delete, name="delete")
]
