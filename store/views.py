
from django.shortcuts import render

def storehome(request):
    return render (request, 'storehome.html',{})