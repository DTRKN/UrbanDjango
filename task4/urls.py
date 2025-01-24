from django.urls import path
from .views import GamesView, CartView, PlatformView

app_name = 'task4'

urlpatterns = [
    path('', PlatformView.as_view(), name='platform'),
    path('games/', GamesView.as_view(), name='games'),
    path('cart/', CartView.as_view(), name='cart'),
]