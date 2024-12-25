from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'cars/home.html')

def car_list(request):
    # Здесь можно добавить логику для получения списка машин
    return render(request, 'cars/car_list.html')

def car_detail(request, car_id):
    # Здесь можно добавить логику для получения деталей конкретной машины
    return render(request, 'cars/car_detail.html', {'car_id': car_id})

def about(request):
    return render(request, 'cars/about.html')

def contact(request):
    return render(request, 'cars/contact.html')
