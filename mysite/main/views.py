from django.shortcuts import render

# Create your views here.

data={
    'title': 'Главная',
    'values': ['some', 'none', 'lorem']
}

def index(request):
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

