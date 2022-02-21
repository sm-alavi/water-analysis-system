from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from . import forms
# Create your views here.

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            None
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
       
    context={}
    return render(request, 'user/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def userLoad(request):
    user=User.objects.all()
    context={'user':user}
    return render(request, 'user/user.html', context)

def userCreate(request):
    form = forms.UserForms()
    context={'form':form,
             'width':500}
    if request.method=="POST":
        form = forms.UserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')

    return render(request, 'form.html', context)

def userUpdate(request, pk):
    user=User.objects.get(id=int(pk))
    form=forms.UserChangeForm(instance=user)
    context={'form':form}
    if request.method=="POST":
        form = forms.UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')

    return render(request, 'form.html', context)

def userDelete(request, pk):
    
    user=User.objects.get(id=int(pk))
    if request.user != user:
        user.delete()
    return redirect('user')

def profileUpdate(request):
    user=User.objects.get(id=int(request.user.id))
    form=forms.UserProfileForm(instance=user)
    context={'form':form}
    if request.method=="POST":
        form = forms.UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, 'form.html', context)

def userActivity(request):
    activity = LogEntry.objects.all()
    print(activity)

    return render(request, 'user/activity.html', {})
