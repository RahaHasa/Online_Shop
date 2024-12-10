# models.py
from django.db import models

class ChatMessage(models.Model):
    is_bot = models.BooleanField(default=False)  # Это поле указывает, является ли сообщение от бота
    message = models.TextField()  # Поле для хранения текста сообщения
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания сообщения

    def __str__(self):
        return self.message
