from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomerInp,CustomerVlanInp,WorkOrderInp,BuildingForm,CommsForm,OfficeForm
from .models import Customer,CustomerVlan,WorkOrder,Building,Room,CommmunicationRoom
from django.shortcuts import redirect, render, get_object_or_404
# Create your views here.


@login_required
def DeviceHome(request):
    return render(request, 'admin/home.html')


######################################### CUSTOMER ######################################################
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

######################################### CUSTOMER ######################################################



######################################### CUSTOMERVLAN ######################################################
def CustomerVlans(request):
    customerVlan = CustomerVlan.objects.all()
    dic = {
        'customerVlan': customerVlan, 
    }
    return render(request, 'admin/customerVlan/CustomerVlan.html', {'dic': dic})

def CustomerVlanInput(request):
    if request.method == "POST":
        form = CustomerVlanInp(request.POST)

        if form.is_valid():        
            form = form.save() 

            return redirect('device:customerVlanlist')
        else:
            pass
    else:
        form = CustomerVlanInp()
        
    dic = {
        'form': form, 
    }
    return render(request, 'admin/customervlan/addcustomerVlan.html', {'dic': dic})

def CustomerVlanInd(request, customerVlan_id):
    customerVlan = CustomerVlan.objects.filter(id = customerVlan_id)

    dic = {
        'customerVlan': customerVlan, 
    }

    return render(request, 'admin/customervlan/indcustomerVlan.html', {'dic': dic})

def CustomerVlanDel(request,customerVlan_id):
    c = CustomerVlan.objects.get(pk=customerVlan_id)
    c.delete()
    return redirect('device:customerVlanlist') 

def CustomerVlanUpd(request,customerVlan_id):
    update = CustomerVlan.objects.get(pk=customerVlan_id)
    form = CustomerVlanInp(instance=update)
    if request.method =='POST':
        form = CustomerVlanInp(request.POST, instance=update)
        
        if form.is_valid():
            form.save()
            return redirect('device:customerVlanlist')
    
    dic = {
        'id': update,
        'form': form,
        
    }

    return render(request, 'admin/customervlan/customerupdVlan.html',{'dic': dic})
######################################### CUSTOMERVLAN ######################################################

######################################### WORKORDER ######################################################
def WorkOrders(request):
    WorkOrders = WorkOrder.objects.all()
    dic = {
        'workorder': WorkOrders, 
    }
    return render(request, 'admin/WorkOrder/workorder.html', {'dic': dic})

def WorkOrderInput(request):
    filter = CustomerVlan.objects.filter(disconnection_date__isnull=True)

    print(filter)
    if request.method == "POST":
        form = WorkOrderInp(request.POST)
        email_extra_body = request.POST['option']
        print(email_extra_body)
        filte = CustomerVlan.objects.get(id = email_extra_body)
        print(filte)
        if form.is_valid():  
            # select = form.cleaned_data['hi']   
            # print(select)   
            form = form.save(commit=False) 
            form.vlan_number = filte

            form.save()

            return redirect('device:workorderlist')
        else:
            pass
    else:
        form = WorkOrderInp()
        
    dic = {
        'form': form, 
        'filter':filter
    }
    return render(request, 'admin/WorkOrder/addworkorder.html', {'dic': dic})

def WorkOrderInd(request, workorder_id):
    workorder = WorkOrder.objects.filter(id = workorder_id)

    dic = {
        'workorder': workorder, 
    }

    return render(request, 'admin/WorkOrder/indworkorder.html', {'dic': dic})

def WorkOrderDel(request,workorder_id):
    c = WorkOrder.objects.get(pk=workorder_id)
    c.delete()
    return redirect('device:workorderlist') 

def WorkOrderUpd(request,workorder_id):
    filter = CustomerVlan.objects.filter(disconnection_date__isnull=True)
    update = WorkOrder.objects.get(pk=workorder_id)
    form = WorkOrderInp(instance=update)
    if request.method =='POST':
        form = WorkOrderInp(request.POST, instance=update)
        email_extra_body = request.POST['option']
        print(email_extra_body)
        filte = CustomerVlan.objects.get(id = email_extra_body)
        print(filte)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            WorkOrder.objects.filter(pk=workorder_id).update(vlan_number =filte)
            return redirect('device:workorderlist')
    
    dic = {
        'id': update,
        'form': form,
        'filter':filter,
        
    }

    return render(request, 'admin/WorkOrder/workorderupd.html',{'dic': dic})
######################################### WORKORDER ######################################################


######################################### CUSTOMERVLAN ######################################################
def Location(request):
    building = Building.objects.all()
    office = Room.objects.all()
    commsroom = CommmunicationRoom.objects.all()
    dic = {
        'building': building,
        'office' : office,
        'comms' : commsroom 
    }
    return render(request, 'admin/location/locationlist.html', {'dic': dic})

def BuildingInput(request):
    if request.method == "POST":
        form = BuildingForm(request.POST)

        if form.is_valid():        
            form = form.save() 

            return redirect('device:locationlist')
        else:
            pass
    else:
        form = BuildingForm()
        
    dic = {
        'form': form, 
    }
    return render(request, 'admin/location/addbuilding.html', {'dic': dic})

def BuildingDel(request,building_id):
    c = Building.objects.get(pk=building_id)
    c.delete()
    return redirect('device:locationlist') 

def BuildingUpd(request,building_id):
    update = Building.objects.get(pk=building_id)
    form = BuildingForm(instance=update)
    if request.method =='POST':
        form = BuildingForm(request.POST, instance=update)
        
        if form.is_valid():
            form.save()
            return redirect('device:locationlist')
    
    dic = {
        'id': update,
        'form': form,
        
    }

    return render(request, 'admin/location/updbuilding.html',{'dic': dic})
######################################### CUSTOMERVLAN ######################################################


######################################### CUSTOMERVLAN ######################################################

def OfficeInput(request):
    if request.method == "POST":
        form = OfficeForm(request.POST)

        if form.is_valid():        
            form = form.save() 

            return redirect('device:locationlist')
        else:
            pass
    else:
        form = OfficeForm()
        
    dic = {
        'form': form, 
    }
    return render(request, 'admin/location/addoffice.html', {'dic': dic})

def OfficeDel(request,office_id):
    c = Room.objects.get(pk=office_id)
    c.delete()
    return redirect('device:locationlist') 

def OfficeUpd(request,office_id):
    update = Room.objects.get(pk=office_id)
    form = OfficeForm(instance=update)
    if request.method =='POST':
        form = OfficeForm(request.POST, instance=update)
        
        if form.is_valid():
            form.save()
            return redirect('device:locationlist')
    
    dic = {
        'id': update,
        'form': form,
        
    }

    return render(request, 'admin/location/updoffice.html',{'dic': dic})
######################################### CUSTOMERVLAN ######################################################


######################################### CUSTOMERVLAN ######################################################

def CommsInput(request):
    if request.method == "POST":
        form = CommsForm(request.POST)

        if form.is_valid():        
            form = form.save() 

            return redirect('device:locationlist')
        else:
            pass
    else:
        form = CommsForm()
        
    dic = {
        'form': form, 
    }
    return render(request, 'admin/location/addcomsroom.html', {'dic': dic})

def CommsDel(request,comms_id):
    c = CommmunicationRoom.objects.get(pk=comms_id)
    c.delete()
    return redirect('device:locationlist') 

def CommsUpd(request,comms_id):
    update = CommmunicationRoom.objects.get(pk=comms_id)
    form = CommsForm(instance=update)
    if request.method =='POST':
        form = CommsForm(request.POST, instance=update)
        
        if form.is_valid():
            form.save()
            return redirect('device:locationlist')
    
    dic = {
        'id': update,
        'form': form,
        
    }

    return render(request, 'admin/location/updcomms.html',{'dic': dic})
######################################### CUSTOMERVLAN ######################################################




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