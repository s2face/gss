from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index),
    path('ls', views.ls),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]