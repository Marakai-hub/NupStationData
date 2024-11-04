from django.contrib import admin
from django.urls import path, include
from agents import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.agent_list, name='agent_list'),  # Root URL for agent list
]
