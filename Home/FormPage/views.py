from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Form, FileInput
# Create your views here.


def FormPage(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            bigform = form.save() 
            
        else:
            print(form.is_bound)
            print(form.is_valid())
            print(form.errors)
        
        for f in request.FILES.getlist('files'):
            inputs = FileInput(request.FILES, request.POST)
            if inputs.is_valid():
                print(f'yo this is working {f}')
                fileinp = inputs.save(commit=False)
                fileinp.files = f
                fileinp.form_fk = bigform
                fileinp.save()
            else:
                print(inputs.is_valid())
                print(inputs.is_bound)
                print(inputs.errors)
                
        return HttpResponseRedirect('/help/') 
    else:
        form = Form()
        inputs = FileInput()
    
    dic = {
        'form': form,
        'fileinputs': FileInput
    }
    return render(request, 'formpage.html', {'dic': dic})