from django.urls import path
from . import views

urlpatterns=[
    path('meme/', views.MemeView.as_view(), name='meme'),
    path('delayed_name/', views.delay_name, name='delayed_name'),
]