from django.shortcuts import render

import request 

def home(request):
    response = request.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'core/home.html',{
        'ip': geodate['ip'],
        'country': geodata['country_name']
    })