from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    num1 = 10
    num2 = 20
    result = num1 + num2
    return HttpResponse(f"10 + 10 = {result}")

def news(request):
    text = "Инфо о гиксе"
    return HttpResponse(text)