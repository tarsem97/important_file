"""django_perfect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app_claiming.views import login,sign_up,dashboard,logout,perfect,create_response_message,view_response_message,delete_response_message,update_response_message
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login, name='login'),
    path('signup/',sign_up, name='sign_up'),
    path('dashboard/',dashboard, name='dashboard'),
    path('perfect/',perfect, name='perfect'),
    path('logout/',logout, name='logout'),
    path('create-response-message/',create_response_message, name='create_response_message'),
    path('view-response-message/',view_response_message, name='view_response_message'),
    path('delete-response-message/<int:id>/', delete_response_message, name='delete_response_message'),
    path('update-response-message/<int:id>/', update_response_message, name='update-response-message'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)