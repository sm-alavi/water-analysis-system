from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.hashers import make_password
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
        print(user)
        if user is not None:
            login(request, user)
            print('login shod')
            return redirect('dashboard')
       
    context={}
    return render(request, 'user/login.html', context)

@login_required
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required
def userLoad(request):
    user=User.objects.all()
    context={'user':user}
    return render(request, 'user/user.html', context)

@login_required
def userCreate(request):
    form = forms.UserForms()
    context={'form':form,
             'width':500}
    if request.method=="POST":
        form = forms.UserForms(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.password = make_password(request.POST.get("password"))
            form.save()
            return redirect('user')

    return render(request, 'form.html', context)

@login_required
def userUpdate(request, pk):
    user=User.objects.get(id=int(pk))
    form=forms.UserChangeForm(instance=user)
    context={'form':form}
    if request.method=="POST":
        form = forms.UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user')

    return render(request, 'user/userform.html', context)

@login_required
def userDelete(request, pk):
    
    user=User.objects.get(id=int(pk))
    if request.user != user:
        user.delete()
    return redirect('user')

@login_required
def profileUpdate(request):
    user=User.objects.get(id=int(request.user.id))
    form=forms.UserProfileForm(instance=user)
    context={'form':form}
    if request.method=="POST":
        form = forms.UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"Your profile updated succesfully!")

            return redirect('profile')

    return render(request, 'user/userform.html', context)

@login_required
def userActivity(request):
    activity = LogEntry.objects.all()
    print(activity)

    return render(request, 'user/activity.html', {})
