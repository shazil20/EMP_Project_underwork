"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from employee import views
from employee.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)






urlpatterns = [

    # Swagger ui urls
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    # employee urls
    path('employee/', include('employee.urls')),




    path('djadmin/', admin.site.urls),
    # path('admin/', include('customadmin.urls')),
    path('createuser/', views.createuser, name='createuser'),
    path('login/', views.admin_login, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('generate_salary_slip/', views.generate_salary_slip, name='generate_salary_slip'),
    path('apply_leave/', views.apply_leave, name='apply_leave'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('listuser/', listuser, name='listuser'),
    path('edit_employee/', edit_employee, name='edit_employee'),
    path('edit_employee/<int:user_id>/', edit_employee_detail, name='edit_employee_detail'),
    path('user/<int:user_id>/details/', userdetails, name='userdetails'),

    path('employee/delete/<int:pk>/', delete_employee, name='delete_employee'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
