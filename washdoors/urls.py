"""washdoors URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from .views import TrailViews
from .views import CustomerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomerView.home, name='home'),
    path('contact/', CustomerView.contact, name='home'),
    path('cust/login/',CustomerView.custLogin,name="Customer_Login"),
    path('cust/dashboard/',CustomerView.dashboard,name='customerDashboard'),

    path('trail/', TrailViews.trail, name='trail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
