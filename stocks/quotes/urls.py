"""Routing module"""
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
	path('accounts/', include("django.contrib.auth.urls")),
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("delete/<stock_id>", views.delete, name="delete"),
    path("download/", views.download_csv, name="download")
]
