from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):

    print(request.GET.urlencode())
    return HttpResponse('ok')