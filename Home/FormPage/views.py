from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Form, FileInput


from django.contrib.auth.decorators import login_required
# Create your views here.


def FormPage(request):

    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            bigform = form.save() 
            print(f'is this even working {form}')
            for f in request.FILES.getlist('files'):
                inputs = FileInput(request.FILES, request.POST)
                if inputs.is_valid():
                    fileinp = inputs.save(commit=False)
                    fileinp.files = f
                    fileinp.form_fk = bigform
                    fileinp.save()
                else:
                    print(inputs.is_valid())
                    print(inputs.is_bound)
                    print(inputs.errors)
            return redirect('Form:thanks')
        else:
            print(form.is_bound)
            print(form.is_valid())
            print(form.errors)
    else:
        form = Form()
        inputs = FileInput()
    
    dic = {
        'form': form,
        'fileinputs': FileInput
    }
    return render(request, 'formpage.html', {'dic': dic})


def ThanksPage(request):
    return render(request, 'thank_page.html')


@login_required
def AdminPage(request):
    return render(request, 'admin/admin-view.html')