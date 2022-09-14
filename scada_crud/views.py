from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from scada_crud.models import Account
# Create your views here.


posts = [
    { 
        'author': 'Sapan Sharma',
        'title': 'World, Meet SCADOr!',
        'content': 'First post content',
        'postedDate': '12 September 2022'
    },
    {
        'author': 'Sapan Sharma',
        'title': 'With the dawn of Industry 4.0, So many more options are here',
        'content': 'Second post content',
        'postedDate': '13 September 2022'
    }
]

def home(request):
    context = {'posts': posts}
    return(render(request, 'scada_crud/home.html', context))

def assembly(request):
    return(HttpResponse('<h2>This will show a table of assembly lines of your factory</h2>'))

def accounts(request):
    accounts = {'accounts': Account.objects.all}
    return( render(request, 'scada_crud/accounts.html', accounts))

