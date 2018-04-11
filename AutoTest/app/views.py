from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    """
    zheshi zhuyemiande
    :param request:
    :return:
    """
    return render(request,'index.html')

def login(request):
    """
    :param request:
    :return:
    """
    return render(request,'login.html')
