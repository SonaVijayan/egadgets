from django.shortcuts import render,redirect
from django.views import View
from .forms import LoginForm,RegForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.
class LandingView(View):
    def get(self,request):
        return render(request,"landing.html")

class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        form=LoginForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pswd=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                return HttpResponse("Login Success")
            else:
                messages.error(request,"Login Failed!!!,,Invalid Username/Password")
                return redirect('log')
        return render(request,"login.html",{"form":form})
        


class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request):
        formdata=RegForm(data=request.POST)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"Registration Successfull!!!")
            return redirect('log')
        messages.error(request,"Registration Failed!!!")
        return render(request,"reg.html",{"form":formdata})

