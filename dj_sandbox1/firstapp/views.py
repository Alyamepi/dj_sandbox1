from django.shortcuts import render
from django.http import HttpResponse
from .forms import AskNumber

# def home(request):
#     return HttpResponse('Home page')


def home(request):
    return render(
        request,
        'firstapp/home.html',
        )


def calc(request):
    if request.method == "POST":
        numberform=AskNumber(request.POST)
        if numberform.is_valid():
            return render(
            request,
            'firstapp/calculator.html',
            {"result" : 2*int(numberform.cleaned_data['n1']), 'get':False}
        )
    
    else:
        
        numberform = AskNumber()
        return render(
            request,
            'firstapp/calculator.html',
             {'asknumber':numberform, 'get':True}
        )

