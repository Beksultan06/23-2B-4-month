from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ux_ui(request):
    text = """UX расшифровывается как «user experience», что в переводе означает «пользовательский опыт»."""
    return HttpResponse(text)