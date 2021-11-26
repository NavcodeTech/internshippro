from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from .form import *

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def home(request):
    details = {'profile' : Profile.objects.all()}
    return render(request, 'home.html' , details)

def logout_user(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

def prof_delete(request,email):
    try:
        pro_obj = Profile.objects.get(email=email)
        pro_obj.delete()

    except Exception as e:
        print(e)
    return redirect('/home/')

def prof_update(request,email):
    context = {}
    try:
        prof_obj = Profile.objects.get(email=email)
        print(prof_obj)

        initial_detail = {'address': prof_obj.address}
        form = UserForm(initial=initial_detail)
        if request.method == 'POST':
            form = UserForm(request.POST,instance=prof_obj)
            email = request.POST.get('email')
            username=request.user

            if form.is_valid():
                address = form.cleaned_data['address']
                form.save()
                return HttpResponseRedirect("/home/")
            else:
                form=UserForm()

        context['prof_obj'] = prof_obj
        context['form'] = form

    except Exception as e:
        print(e)
    return render(request, 'prof_update.html', context)
