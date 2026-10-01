"""
URL configuration for itu project.

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
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),  
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("projects/", TemplateView.as_view(template_name="projects.html"), name="projects"),
    path("other/", TemplateView.as_view(template_name="other.html"), name="other"),
    path("pictures/", TemplateView.as_view(template_name="pictures.html"), name="pictures"),
    path("education/", TemplateView.as_view(template_name="education.html"), name="education"),
    path("erasmus/", TemplateView.as_view(template_name="erasmus.html"), name="erasmus"),
    path("staff/", TemplateView.as_view(template_name="staff.html"), name="staff"),
    path("place/", TemplateView.as_view(template_name="place.html"), name="place"),
    path("history/", TemplateView.as_view(template_name="history.html"), name="history"),
    path("harezmi/", TemplateView.as_view(template_name="harezmi.html"), name="harezmi"),
    path("timetable/", TemplateView.as_view(template_name="timetable.html"), name="timetable"),
]
