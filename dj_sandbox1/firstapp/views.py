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
        number=AskNumber(request.POST)
        if number.is_valid():
            return render(
            request,
            'firstapp/result.html',
            {"result" : 2*int(number.cleaned_data['n1']),}
        )
    
    else:
        number = AskNumber()
        return render(
            request,
            'firstapp/calculator.html',
             {'number':number}
        )

