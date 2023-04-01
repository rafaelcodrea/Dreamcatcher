from django.http import HttpResponse
from django.shortcuts import render
from .models import Dream
import matplotlib.pyplot as plt

# Create your views here.
#request handler
#request -> response

import logging
logger = logging.getLogger("mylogger")



def duration_chart(request):
    # get the data from the database
    durations = Dream.objects.values_list('duration', flat=True)
    
    # create a histogram
    fig, ax = plt.subplots()
    ax.hist(durations, bins=[1, 2, 3, 4, 5, 6], align='left')
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(['1', '2', '3', '4', '5'])
    ax.set_xlabel('Duration')
    ax.set_ylabel('Count')
    ax.set_title('Duration Chart')

    # convert the plot to a Django-compatible format
    from io import BytesIO
    import base64
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    return render(request, 'duration_chart.html', {'data': data})

def index(request):
    if request.method == 'POST':
        description = request.POST['description']
        duration = request.POST['duration']
        stress_level = request.POST['stress_level']
        energy = request.POST['energy']
        
        dream = Dream(description=description, duration=duration, stress_level=stress_level, energy=energy)
        logger.info("Whatever to log")
        dream.save()
        return render(request, 'hello.html')
    
    # If the request is a GET request, render the index template
    return render(request, 'hello.html')

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Rafael'})
