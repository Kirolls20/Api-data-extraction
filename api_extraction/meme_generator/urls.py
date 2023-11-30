from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('meme/', views.MemeView.as_view(), name='meme'),
    path('delayed_name/', views.delay_meme, name='delayed_name'),
    path('quote/',views.QuoteView.as_view(),name='quote'),
    path('quote-api/',views.api_quote,name='api_quotes'),
]