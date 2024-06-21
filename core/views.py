from django.shortcuts import render
import requests
import json

def home(request):
    with open('mb.json', 'r') as json_file:
        data = json.load(json_file)

    ip_address = data.get('ip')
    country_name = data.get('country_name')

    return render(request, 'core/home.html', {
        'ip': ip_address,
        'country': country_name
    })
