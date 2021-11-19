from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Form
# Create your views here.


def FormPage(request):
    if request.method == "POST":
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.is_bound)
            print(form.is_valid())
            print(form.errors)
        return HttpResponseRedirect('/help/')
    else:
        form = Form()
        
    dic = {
        'form': form,
    }
    return render(request, 'formpage.html', {'dic': dic})