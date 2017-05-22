from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href='api/v1'>API</a>")