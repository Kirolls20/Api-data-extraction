import requests
import json
import random
import time
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class HomeView(TemplateView):
    template_name = 'home.html'

@method_decorator(csrf_exempt, name='dispatch')
class MemeView(TemplateView):
    template_name = 'meme.html'

    @staticmethod
    def extract_meme():
        url = 'https://api.memegen.link/templates'
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(requests.request('GET',url).text)
            names = [name['name'] for name in data]
            pics = [pic['blank'] for pic in data]
            meme_dict = {'name':names,'pic':pics}
            
            return meme_dict
        else:
           return [],[]
@csrf_exempt
def delay_meme(request):
    if request.method == 'GET':
        names = MemeView.extract_meme()
        delayed_names = []
        for name,pic in zip(names['name'],names['pic']):
            # time.sleep(20)
            delayed_names.append({'name':name,'pic':pic}) 
        random.shuffle(delayed_names)
        return JsonResponse({'names': delayed_names})
    else:
        return JsonResponse({'error': 'Invalid request method'})


@method_decorator(csrf_exempt, name='dispatch')
class QuoteView(TemplateView):
    template_name= 'quote.html'

    @staticmethod
    def extract_quote():
        url = 'https://gist.githubusercontent.com/nasrulhazim/54b659e43b1035215cd0ba1d4577ee80/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json'
        response = requests.get(url)
        if response.status_code == 200:
            response = json.loads(requests.request("GET",url).text)
            data = response.get('quotes',[])
            quotes = [quote['quote'] for quote in data]
            authors = [author['author'] for author in data]
            dict_data = {'quote':quotes,'author':authors}
            return dict_data
        else: 
            return []

@csrf_exempt
def api_quote(request):
    if request.method =='GET':
        data = QuoteView.extract_quote()
        print(data)
        delayed_quotes = []
        for quote,author in zip(data['quote'],data['author']):
            delayed_quotes.append({'quote':quote,'author':author})
            random.shuffle(delayed_quotes)
        return JsonResponse({'quotes':delayed_quotes})
    else:
        return JsonResponse({'error': 'Invalid request method'})









