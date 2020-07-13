from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template

# Create your views here.
def home(request):
    # return HttpResponse("Hello, Django!")
    # data = {'first': 'Sanghun', 'second': 'Oh'}
    data = request.GET.copy()         # ?first=Sanghun&second=Oh
    print(data)
    # data['result'] = cal(data['first'], data['second'])
    data['result'] = XORwithKeras(data['first'], data['second'])
    return render(request, 'hello/home.html', context=data)

def form(request):
    data = request.GET.copy() 
    return render(request, 'hello/form.html', context=data)

def cal(first, second):
    result = int(first) * int(second)
    return result

import tensorflow as tf
def XORwithKeras(first, second):
    new_model = tf.keras.models.load_model('hello/XORwithKeras.h5')
    param = [int(first), int(second)]
    result = new_model.predict([param])
    return result    