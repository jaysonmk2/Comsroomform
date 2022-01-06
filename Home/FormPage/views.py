import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .forms import Form, FileInput
from .models import Form as Forms, FormFiles


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

    # end_time__lt, the lt means lesser than and if you see gt it means greater than
    active = Forms.objects.filter(approved_or_not= "APPROVED").exclude(end_time__lt=datetime.date.today())
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

    # gt means greater than
    pending = Forms.objects.exclude(end_time__gt=datetime.date.today()).filter(required_access="TEMPORARY")
    dic = {
        'signed_up':pending,
    }
    return render(request, 'admin/admin-view.html', {'dic': dic})

# end_time__gt=datetime.date.today(), 

@login_required
def ViewUser(request, form_id):
    # gt means greater than
    user_detail = get_object_or_404(Forms, pk=form_id)
    files = FormFiles.objects.filter(form_fk_id = form_id)
    dic = {
        'user_detail':user_detail,
        'user_files':files,
    }
    return render(request, 'admin/admin-view-user-detail.html', {'dic': dic})

 