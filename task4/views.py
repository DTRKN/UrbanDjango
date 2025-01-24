from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class GamesView(TemplateView):
    template_name = "fourth_task/games.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ['Cyberpunk 2077', 'Elden Ring', 'God of War']
        return context

class CartView(TemplateView):
    template_name = "fourth_task/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = []
        return context


class PlatformView(TemplateView):
    template_name = "fourth_task/platform.html"