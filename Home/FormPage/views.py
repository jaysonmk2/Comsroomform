import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .forms import Form, FileInput
from .models import Form as Forms


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
        'fileinputs': FileInput,
    }
    return render(request, 'formpage.html', {'dic': dic})


def ThanksPage(request):
    return render(request, 'thank_page.html')


@login_required
def AdminPage(request):
    signed_up = Forms.objects.all()
    dic = {
        'signed_up':signed_up,
    }
    return render(request, 'admin/admin-view.html', {'dic': dic})

@login_required
def Active(request):
    active = Forms.objects.filter(approved_or_not= "APPROVED")
    dic = {
        'signed_up':active,
    }
    return render(request, 'admin/admin-view.html', {'dic': dic})

@login_required
def Pending(request):
    pending = Forms.objects.filter(approved_or_not = None)
    dic = {
        'signed_up':pending,
    }
    return render(request, 'admin/admin-view.html', {'dic': dic})


@login_required
def Eliminated(request):
    pending = Forms.objects.exclude(end_time__gt=datetime.date.today()).filter(required_access="TEMPORARY")
    dic = {
        'signed_up':pending,
    }
    return render(request, 'admin/admin-view.html', {'dic': dic})


# end_time__gt=datetime.date.today(), 

