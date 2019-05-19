from django.http import HttpResponse
from django.shortcuts import render
import os
def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

