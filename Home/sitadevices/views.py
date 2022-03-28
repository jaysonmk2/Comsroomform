from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomerInp
from .models import Customer
from django.shortcuts import redirect, render, get_object_or_404
# Create your views here.


@login_required
def DeviceHome(request):
    return render(request, 'admin/home.html')


def CustomerViews(request):
    customer = Customer.objects.all()
    dic = {
        'customer': customer, 
    }
    return render(request, 'admin/Customer.html', {'dic': dic})

def CustomerInput(request):
    if request.method == "POST":
        form = CustomerInp(request.POST)

        if form.is_valid():        
            form = form.save() 

            return redirect('device:customerlist')
        else:
            pass
    else:
        form = CustomerInp()
        
    dic = {
        'form': form, 
    }
    return render(request, 'admin/addcustomer.html', {'dic': dic})

def CustomerInd(request, customer_id):
    customer = Customer.objects.filter(id = customer_id)

    dic = {
        'customer': customer, 
    }

    return render(request, 'admin/indcustomer.html', {'dic': dic})

def CustomerDel(request,customer_id):
    c = Customer.objects.get(pk=customer_id)
    c.delete()
    return redirect('device:customerlist') 

def CustomerUpd(request,customer_id):
    update = Customer.objects.get(pk=customer_id)
    form = CustomerInp(instance=update)
    if request.method =='POST':
        form = CustomerInp(request.POST, instance=update)
        
        if form.is_valid():
            form.save()
            return redirect('device:customerlist')
    
    dic = {
        'id': update,
        'form': form,
        
    }

    return render(request, 'admin/customerupd.html',{'dic': dic})
    
#  def SwitchForm(request):
#     if request.method == "POST":
#         port_amount = int(request.POST.get('port-amount'))
#         form = SwitchInp(request.POST)
        
        
#         print(port_amount)
#         if form.is_valid():
#             port_count = 0
#             bigform = form.save() 
            
#             for n in range(port_amount):
#                 port = Port(port_number = port_count,port_desc='', associate='switch',status=False, switch_id=bigform.id)
#                 port.save()
#                 port_count = port_count + 1
            
#             port_count = 0

#             return redirect('device:switchInp')
#         else:
#             pass
#     else:
#         form = SwitchInp()
        
#     dic = {
#         'form': form, 
#     }
#     return render(request, 'admin/addswitch.html', {'dic': dic})