from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_with_gpt, name='chat'),  # Этот путь будет использоваться в форме
]
