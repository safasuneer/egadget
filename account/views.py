from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView,CreateView
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
# class EHomeView(View):
#     def get(self,request):
#         form=LoginForm()
#         return render(request,"ehome.html",{"form":form})

class EHomeView(FormView):
    template_name="ehome.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            print(user)
            if user:
                login(request,user)
                return redirect("custhome")
            else:
                messages.error(request,"Sigh in failed!!")
                return redirect('home')
        return render(request,"ehome.html",{"form":form_data})


class UserRegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request,"Registration Successfull!!")
        return super().form_valid(form)
    
    

    
# class UserRegView(View):
#     def get(self,request):
#         f=RegForm()
#         return render(request,"reg.html",{"form":f})
#     def post(self,request):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"Sigh Up Completed!")
#             return redirect("home")
#         return render(request,"reg.html",{"form":form_data})

class LgOutView(View):
    def get(self,request):
        logout(request)
        return redirect("home")
    
