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
def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'core/github.html', {'user': user})