import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .forms import Form, FileInput
from .models import Form as Forms, FormFiles
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from django.template.loader import get_template




from django.contrib.auth.decorators import login_required
# Create your views here.


def FormPage(request):
    if request.method == "POST":
        form = Form(request.POST)
        
        if form.is_valid():
            bigform = form.save() 
            dic = {
                    'body': 'A user has filled in a form',
                    'approved_or_rejected': '',
                    'approved_or_rejected_text': ''
                }
            html_tpl_path = 'email-template/email.html'
            context_data =  {'dic': dic}
            email_html_template = get_template(html_tpl_path).render(context_data)
            receiver_email = 'nullwandere@gmail.com'
            email_msg = EmailMessage('New user Application', 
                                        email_html_template, 
                                        settings.APPLICATION_EMAIL,
                                        [receiver_email],
                                        reply_to=[settings.APPLICATION_EMAIL]
                                        )
            # this is the crucial part that sends email as html content but not as a plain text
            email_msg.content_subtype = 'html'
            email_msg.send(fail_silently=False)
            
            for f in request.FILES.getlist('files'):
                inputs = FileInput(request.FILES, request.POST)
                if inputs.is_valid():
                    fileinp = inputs.save(commit=False)
                    fileinp.files = f
                    fileinp.form_fk = bigform
                    fileinp.save()
                else:
                  pass
            return redirect('Form:thanks')
        else:
            pass
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
    pending = Forms.objects.filter(approved_or_not = None).exclude(end_time__lt=datetime.date.today())
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
    user = Forms.objects.get(id=form_id)

    form = Form(instance=user)
    if request.method =='POST':
        form = Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            approved_or_not = form.cleaned_data['approved_or_not']
            email_extra_body = request.POST['email-send']

            # APPROVED

            if approved_or_not == 'APPROVED':
                dic = {
                    'body': email_extra_body,
                    'approved_or_rejected': 'Approved',
                    'approved_or_rejected_text': 'You have been approved access to the Hato Communication rooms'
                }
                html_tpl_path = 'email-template/email.html'
                context_data =  {'dic': dic}
                email_html_template = get_template(html_tpl_path).render(context_data)
                receiver_email = email
                email_msg = EmailMessage('Welcome from airport Coms', 
                                            email_html_template, 
                                            settings.APPLICATION_EMAIL,
                                            [receiver_email],
                                            reply_to=[settings.APPLICATION_EMAIL]
                                            )
                # this is the crucial part that sends email as html content but not as a plain text
                email_msg.content_subtype = 'html'
                email_msg.send(fail_silently=False)
                # send_mail(
                #     'Subject here',
                #     f'You have been approved to enter the HATO communication rooms \n {email_extra_body}',
                #     'airporttesting@outlook.com',
                #     [email,],
                # )
            else:
                dic = {
                    'body': email_extra_body,
                    'approved_or_rejected': 'Rejected',
                    'approved_or_rejected_text': 'You have been Rejected to access the Hato Communication rooms'
                }
                html_tpl_path = 'email-template/email.html'
                context_data =  {'dic': dic}
                email_html_template = get_template(html_tpl_path).render(context_data)
                receiver_email = email
                email_msg = EmailMessage('Welcome from airport Coms', 
                                            email_html_template, 
                                            settings.APPLICATION_EMAIL,
                                            [receiver_email],
                                            reply_to=[settings.APPLICATION_EMAIL]
                                            )
                # this is the crucial part that sends email as html content but not as a plain text
                email_msg.content_subtype = 'html'
                email_msg.send(fail_silently=False)
                
                # send_mail(
                #     'Subject here',
                #     f'You have been rejected \n {email_extra_body}',
                #     'airporttesting@outlook.com',
                #     [email,],
                # )
            return redirect('Form:adminpage')   

    dic = {
        'user_detail':user_detail,
        'user_files':files,
        'form':form,
    }
    return render(request, 'admin/admin-view-user-detail.html', {'dic': dic})

 
@login_required
def MasterAdmin(request):
    return render(request, 'admin/master-admin.html')
