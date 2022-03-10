from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SwitchInp
from .models import Port
from django.shortcuts import redirect, render, get_object_or_404
# Create your views here.

@login_required
def DeviceHome(request):
    return render(request, 'admin/home.html')

def SwitchForm(request):
    if request.method == "POST":
        port_amount = int(request.POST.get('port-amount'))
        form = SwitchInp(request.POST)
        
        
        print(port_amount)
        if form.is_valid():
            port_count = 0
            bigform = form.save() 
            
            for n in range(port_amount):
                port = Port(port_number = port_count,port_desc='', associate='switch',status=False, switch_id=bigform.id)
                port.save()
                port_count = port_count + 1
            
            port_count = 0

            # for f in request.FILES.getlist('files'):
            #     inputs = FileInput(request.FILES, request.POST)
            #     if inputs.is_valid():
            #         fileinp = inputs.save(commit=False)
            #         fileinp.files = f
            #         fileinp.form_fk = bigform
            #         fileinp.save()
            #     else:
            #       pass
            return redirect('device:switchInp')
        else:
            pass
    else:
        form = SwitchInp()
        
    dic = {
        'form': form, 
    }
    return render(request, 'admin/addswitch.html', {'dic': dic})