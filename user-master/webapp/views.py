from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webapp.forms import signupForm
from webapp.forms import SentForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail,EmailMessage
from django.conf import settings


# Create your views here.
def home_page(request):
    return render(request,'myapp/home.html')


@login_required
def study_material(request):
    return render(request,'myapp/study_material.html')




def logout(request):
    return render(request,'myapp/logout.html')


def registration_view(request):
    form=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST)
        user=form.save(commit=True)
        user.set_password(user.password)
        user.save()

        return HttpResponseRedirect('/accounts/login')
    return render(request,"myapp/registration.html",{'form':form})



def sending_mail(request):

    if request.method == 'POST':
        form = SentForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            mail = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail('got mail from'+str(mail),
                "name: "+str(name)+"\n"
                "email:"+str(mail)+"\n"
                "subject: "+str(sub)+"\n"
                "message :"+ str(message),
                settings.EMAIL_HOST_USER,
                ['shindevikas15@gmail.com'],
                fail_silently=False )
            return HttpResponseRedirect('/')
    else:
        form = SentForm()
    return render(request, "myapp/mail.html", {'form': form})
