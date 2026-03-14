"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from home import views as home_views
from course import views as course_views
from about import views as about_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home),
    path('course/', course_views.course),
    path('about/', about_views.about),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', home_views.logout),
    path('signup/', home_views.signup),
]
