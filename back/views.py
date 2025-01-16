from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def back(request):
    back_info = """Backend — это внутренняя часть продукта,
    которая находится на сервере и скрыта от пользователей.
      Для ее разработки могут использоваться
      самые разные языки, например, Python, PHP, Go, JavaScript, Java, С#."""
    return HttpResponse(back_info)

