"""bluetides URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('simulation/<int:pk>/', views.Simulations.as_view(), name='simulation'),
    path('snapshot/<int:pk>/', views.Snapshot.as_view(), name='snapshot'),
    path('snapshot/<int:pk>/fofgroups/', views.Fofgroups.as_view(), name='fofgroups'),
    path('snapshot/<int:pk>/species/', views.Species.as_view(), name='species'),
    path('download_modal/', views.DownloadModal.as_view(), name='download_modal'),
    path('download_modal/<str:file_requested>/', views.DownloadModal.as_view(), name='download_modal')
]
