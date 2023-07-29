from django.urls import path
from .views import BotView
urlpatterns = [
    
    path("bot",BotView.as_view())
    
]
