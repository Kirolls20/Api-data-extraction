import requests
import json
import random
import time
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


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
def delay_name(request):
    if request.method == 'GET':
        names = MemeView.extract_meme()
        delayed_names = []
        for name,pic in zip(names['name'],names['pic']):
            # time.sleep(20)
            delayed_names.append({'name':name,'pic':pic}) 

        return JsonResponse({'names': delayed_names})
    else:
        return JsonResponse({'error': 'Invalid request method'})