"""got_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from classifieds import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AdList.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('new_ad/', views.new_ad, name='new_ad'),
    path('view/<str:identifier>/', views.view_ad, name='ad_detail'),
    path('edit/<str:identifier>/', views.edit_ad, name='edit'),
    path('delete/<str:identifier>/', views.delete_ad, name='delete'),
    path('save/<str:identifier>/', views.save_ad, name='save'),
    path('profile/', views.Profile.as_view(), name='profile'),
]
