from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import json
from django.core.paginator import Paginator

# Create your views here.
def data(request, page=1):
    # Path to the JSON file
    data_file = Path(__file__).resolve().parent / 'data' / 'webs1.json'

    # Load the JSON data
    with open(data_file, 'r') as file:
        data = json.load(file)

    # Paginate the data (1000 items per page)
    paginator = Paginator(data, 1000)  # 1000 records per page
    page_obj = paginator.get_page(page)

    # Pass the data to the template
    context = {
        'data': data,
        'page_obj': page_obj
    }
    return render(request, 'data.html', context)


def web(request):
    return render(request, 'home.html', {'message': 'Welcome to the Angel Page!'})
def page(request):
    return render(request, 'home.html', {'message': 'Welcome to the Asir Page!'})
def domain(request):
    return render(request, 'home.html', {'message': 'Welcome to the Joshva Page!'})
def home(request):
    return render(request, 'home.html', {'message': 'Welcome to Jonathan Page!'})

