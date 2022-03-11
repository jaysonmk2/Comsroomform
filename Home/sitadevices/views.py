from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SwitchInp
from .models import Port,Switch
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

            return redirect('device:switchInp')
        else:
            pass
    else:
        form = SwitchInp()
        
    dic = {
        'form': form, 
    }
    return render(request, 'admin/addswitch.html', {'dic': dic})

def SwitchViews(request):
    switches = Switch.objects.all()
    dic = {
        'switch': switches, 
    }
    return render(request, 'admin/switchlist.html', {'dic': dic})

def SwitchIndividualView(request, switch_id):
    switches = Switch.objects.filter(id = switch_id)
    
    print(switches)
    dic = {
        'switch': switches, 
    }
    return render(request, 'admin/individualswitch.html', {'dic': dic})
