from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Online-Shop'
        context['content'] = ""
        return context

class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Online-Shop'
        context['content'] = "Добро пожаловать в официальный онлайн-магазин футбольного клуба ACMilan!"
        context['text_on_page'] = (
            "ACMilan – это не просто футбольный клуб, это легенда, символ страсти и стремления к победе. Мы гордимся своей многолетней историей и с честью представляем цвета и символы клуба, который известен и любим по всему миру. "
            "Наш интернет-магазин создан, чтобы каждый поклонник ACMilan мог стать частью этой великой команды и показать свою поддержку, независимо от того, где он находится.\n"
        )
        context['special_offers'] = (
            "Наш магазин предлагает регулярные акции и эксклюзивные предложения для истинных фанатов ACMilan. Вот что вы можете ожидать:\n"
            "\n- Сезонные распродажи: Воспользуйтесь большими скидками на различные товары в течение года. Мы предлагаем особые акции в дни праздников и сезонных распродаж.\n"
            "\n- Скидки для постоянных клиентов: Чем больше покупок вы совершаете, тем больше скидок вы получаете! Участники программы лояльности получают специальные предложения и ранний доступ к новым коллекциям.\n"
            "\n- Ограниченные коллекции: Мы регулярно выпускаем лимитированные издания с уникальным дизайном. Успейте приобрести коллекционные футболки и сувениры, чтобы выделиться среди других фанатов.\n"
            "\n- Сюрпризы и подарки: Мы любим радовать наших покупателей. Совершите покупку и получите шанс получить подарок от ACMilan – будь то брелок, наклейка или другой небольшой сувенир.\n"
            "\n- Подписка на рассылку: Подпишитесь на нашу рассылку, чтобы быть в курсе самых горячих предложений и новых поступлений! Только подписчики получают доступ к эксклюзивным скидкам и предложениям первыми.\n"
        )
        context['categories'] = [
            "Футбольная форма", "Спортивная одежда", "Аксессуары и сувениры", 
            "Оборудование для тренировок", "Электроника и гаджеты", "Коллекционные изделия"
        ]
        
        context['photos'] = [
          {'filename': '1555472.jpg', 'description': 'Исторический момент'},
         
          {'filename': '1555474.jpg', 'description': 'Игровой момент'}
        ]
 

        return context

class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['content'] = "Свяжитесь с нами"
        context['contact_info'] = {
            'phone': '+7 (708) 247-51-31',
            'email': 'hasanbairakhimbaev599.com',
            'address': 'г. Алматы, ул. Аль-Фараби 71/9, д.4, ком.1',
        }
        return context

