"""
URL configuration for khaabgaahh project.

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
from django.urls import path
from core.views import LoginStudent, ReservePanel, logout_user, ChangePasswordView, change_password
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', LoginStudent.as_view(), name='student_login'),
                  path('panel', login_required(ReservePanel.as_view()), name='reserve'),
                  path('logout', logout_user, name='LogOut'),
                  path('change_password', change_password, name='change_password'),


                  path('change_pass/<str:student_number>', ChangePasswordView.as_view(), name='change_pass'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
