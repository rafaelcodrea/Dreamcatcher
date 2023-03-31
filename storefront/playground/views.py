from django.http import HttpResponse
from django.shortcuts import render
from .models import Dream
from .forms import DreamForm

# Create your views here.
#request handler
#request -> response




def index(request):
    if request.method == 'POST':
        form = DreamForm(request.POST)
        if form.is_valid():
            description = request.POST['description']
            duration = request.POST['duration']
            stress_level = request.POST['stress_level']
            energy = request.POST['energy']
            dream = Dream(description=description, duration=duration, stress_level=stress_level, energy=energy)
            dream.save()
            return render(request, 'dreamcatcher/thankyou.html')
    return render(request, 'dreamcatcher/index.html')


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Rafael'})