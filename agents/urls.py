from django.urls import path
from .views import agent_list, agent_detail

urlpatterns = [
    path('', agent_list, name='agent_list'),
    path('agent/<str:agent_id>/', agent_detail, name='agent_detail'),  # Add this line
]
