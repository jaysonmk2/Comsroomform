from django.db import connection
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomerInp,CustomerVlanInp,WorkOrderInp,BuildingForm,CommsForm,OfficeForm,ConnectionsForm,SwitchForm, DataOutletForm
from .models import Customer,CustomerVlan,WorkOrder,Building,Room,CommmunicationRoom, Connections, Switch, DataOutlet
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


######################################### BUILDING ######################################################
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
######################################### BUILDING ######################################################


######################################### OFFICE ######################################################

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
######################################### OFFICE ######################################################


######################################### COMROOM ######################################################

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
######################################### COMROOM ######################################################


######################################### CONNECTION ######################################################
def Connection(request):
    connection = Connections.objects.all()
    dic = {
        'connection': connection, 
    }
    return render(request, 'admin/connection/connection.html', {'dic': dic})

def ConnectionInput(request):
    filter = CommmunicationRoom.objects.all()
    if request.method == "POST":
        form = ConnectionsForm(request.POST)
        com = request.POST['option']
        port_amount = int(request.POST.get('port-amount'))
        patchpanel= int(request.POST.get('patchpanel'))
        print(port_amount)
        filte = CommmunicationRoom.objects.get(id = com)
        print(port_amount)
        if form.is_valid():
            port_count = 1
            bigform = form.save() 
            print(bigform)
            b = Connections.objects.get(id = bigform.id)
            print(b.id)
            for n in range(port_amount):
                port = DataOutlet(connection = b,port_status='ACTIVE',patch_panel=patchpanel,comroom=filte,data_number=port_count)
                port.save()
                port_count = port_count + 1
            
            port_count = 1

            return redirect('device:connectionlist')
        else:
            pass
    else:
        form = ConnectionsForm()
        
    dic = {
        'form': form,
        'filter': filter,
    }
    return render(request, 'admin/connection/addconnection.html', {'dic': dic})

def ConnectionInd(request, connection_id):
    connection = Connections.objects.filter(id = connection_id)
    dataoutlets = DataOutlet.objects.filter(connection = connection_id)
    dic = {
        'connection': connection, 
        'dataoutlets': dataoutlets
    }
    print(dataoutlets)

    return render(request, 'admin/connection/indconnection.html', {'dic': dic})

def ConnectionDel(request,connection_id):
    c = Connections.objects.get(pk=connection_id)
    c.delete()
    return redirect('device:connectionlist') 

def ConnectionUpd(request,connection_id):
    update = Connections.objects.get(pk=connection_id)
    form = ConnectionsForm(instance=update)
    dataoutlet = DataOutlet.objects.filter(connection=connection_id)
    length = len(dataoutlet) 
    filter = CommmunicationRoom.objects.all()
    

    if request.method =='POST':
        com = request.POST['comoption']
        filte = CommmunicationRoom.objects.get(id = com)
        form = ConnectionsForm(request.POST, instance=update)
        option = request.POST['option']
        port_amount = int(request.POST.get('port-amount'))
        # coms= data[1].comroom
        if form.is_valid():
            bigform = form.save() 
            port_count = length + 1
            b = Connections.objects.get(id = bigform.id)
            if option == "add":
                for n in range(port_amount):
                    port = DataOutlet(connection = b,port_status='ACTIVE',patch_panel=0,comroom=filte, data_number=port_count)
                    port.save()
                    port_count = port_count + 1
                
            else:
                numb = length-port_amount
                for n in range(length,numb,-1):
                    c = dataoutlet.get(data_number = n)
                    c.delete()
                
            return redirect('device:connectionlist')
    
    dic = {
        'id': update,
        'form': form,
        'filter': filter,
    }

    return render(request, 'admin/connection/updconnection.html',{'dic': dic})
######################################### CONNECTION ######################################################

######################################### SWITCH ######################################################
def Switchs(request):
    switch = Switch.objects.all()
    dic = {
        'switch': switch, 
    }
    return render(request, 'admin/switch/switch.html', {'dic': dic})

def SwitchInput(request):
    if request.method == "POST":
        form = SwitchForm(request.POST)
        if form.is_valid():  
            form.save()

            return redirect('device:switchlist')
        else:
            pass
    else:
        form = SwitchForm()
        
    dic = {
        'form': form, 
    }
    return render(request, 'admin/switch/addswitch.html', {'dic': dic})

def SwitchInd(request, switch_id):
    switch = Switch.objects.filter(id =switch_id)

    dic = {
        'switch': switch, 
    }

    return render(request, 'admin/switch/indswitch.html', {'dic': dic})

def SwitchDel(request,switch_id):
    c = Switch.objects.get(pk=switch_id)
    c.delete()
    return redirect('device:switchlist') 

def SwitchUpd(request,switch_id):
    
    update =Switch.objects.get(pk=switch_id)
    form = SwitchForm(instance=update)
    if request.method =='POST':
        form = SwitchForm(request.POST, instance=update)
        if form.is_valid():
            
            form.save()
          
            return redirect('device:switchlist')
    
    dic = {
        'id': update,
        'form': form, 
    }

    return render(request, 'admin/switch/updswitch.html',{'dic': dic})
######################################### SWITCH ######################################################

def OutletUpd(request,data_id):
    
    update =DataOutlet.objects.get(pk=data_id)
    form = DataOutletForm(instance=update)
    if request.method =='POST':
        form = DataOutletForm(request.POST, instance=update)
        if form.is_valid():
            
            form.save()
          
            return redirect('device:connectionlist')
    
    dic = {
        'id': update,
        'form': form, 
    }

    return render(request, 'admin/connection/outletupd.html',{'dic': dic})

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