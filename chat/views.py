# chat/views.py

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
import requests

# Настройка ключа API
api_key = settings.MY_API_KEY

# Список для хранения сообщений (можно использовать сессии или базу данных для хранения)
messages = []

def chat_with_gpt(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        
        if user_message:
            # Сохраняем сообщение пользователя
            messages.append({'is_bot': False, 'message': user_message})

            try:
                # Отправка запроса в мой API для получения ответа
                response = requests.post(
                    "https://my-api-endpoint",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "prompt": user_message,
                        "max_tokens": 150,
                        "temperature": 0.7
                    }
                )

                # Ответ от бота
                reply = response.json()["choices"][0]["text"]
                messages.append({'is_bot': True, 'message': reply})
            
            except Exception as e:
                # Обработка ошибок
                messages.append({'is_bot': True, 'message': f"Ошибка: {str(e)}"})
        
        # Отправляем обновленные сообщения в шаблон
        return render(request, 'chat/chat.html', {'messages': messages})
    
    # Если метод запроса не POST, просто отображаем чат с текущими сообщениями
    return render(request, 'chat/chat.html', {'messages': messages})