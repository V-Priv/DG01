from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Это главная страница</h1>")

def data(request):
    return HttpResponse("<h1>Это страничка с данными</h1>")

def test(request):
    return HttpResponse("<h1> Здесь расположены тесты</h1>")
