# pylint: disable=relative-beyond-top-level

"""Routing module"""
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
	path('accounts/', include("django.contrib.auth.urls")),  # noqa:W191
	path('', views.home_view, name="home"),  # noqa:W191
	path('about/', views.about_view, name="about"),  # noqa:W191
	path("dashboard/", views.dashboard_view, name="dashboard"),  # noqa:W191
	path("delete/<stock_id>", views.delete, name="delete"),  # noqa:W191
	path("download/", views.download_csv, name="download"),  # noqa:W191
	path("register/", views.register_user, name="register")  # noqa:W191
]
