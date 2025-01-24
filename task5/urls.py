from django.urls import path
from . import views

urlpatterns = [
    path('signup-django/', views.sign_up_by_django, name='signup_django'),
    path('signup-html/', views.sign_up_by_html, name='signup_html'),
]