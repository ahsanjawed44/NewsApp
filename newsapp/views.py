from django.http import HttpResponse
from django.shortcuts import render
import requests

api_key = 'cf3e763fc3084d2097cde7d87f88cc53'

def home(request):
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    response = requests.get(url)
    
    try:
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        articles = data.get('articles', [])  # Use get method to provide a default empty list
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions
        print(f"Request failed: {e}")
        articles = []

    context = {
        'news': articles
    }
    return render(request, 'index.html', context)
