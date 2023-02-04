"""catalogBackend URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#importing urls
from rest_framework.authtoken.views import obtain_auth_token
from api import views as api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('createUser/',api.createUser,name='user-creation'),
    path('addnremovebook/',api.AddOrRemoveBook,name='add-remove-book'),
    path('getmyinfo/<str:option>/',api.getMyProfileInfo,name='profile-info'),
    path('getmybooks/',api.getMyBooks,name='my-books'),
    path('viewbook/<int:pk>/',api.viewBook,name='view-book'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)