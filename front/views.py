from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def front(request):
    text = """Frontend — это клиентская часть продукта (интерфейс, с которым взаимодействует пользователь)"""
    return HttpResponse(text)