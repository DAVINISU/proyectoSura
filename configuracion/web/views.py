from operator import index
from django.shortcuts import render

# Create your views here.

# renderizar es Pintar
def Home(request):
    return render(request,'index.html')