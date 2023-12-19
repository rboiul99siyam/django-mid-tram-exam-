from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from user_auth.forms import userForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from user_auth.forms import ChangeProfile
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth import  update_session_auth_hash


def register(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Create Successfully ! ")
            return redirect("home")
    else:
        form = userForm()
    return render(request, "register.html", {"form": form, "type": "Sing Up "})


class UserLogIn(LoginView):
    template_name = "register.html"

    def get_success_url(self) -> str:
        return reverse_lazy("showData")

    def form_valid(self, form):
        messages.success(self.request, "Login Successfully !")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Login data incorect !")
        return super().form_invalid(form)

    def get_context_data(self, **kwrags):
        context = super().get_context_data(**kwrags)
        context["type"] = "Login"
        return context


class UserLogOut(LogoutView):
    def get_success_url(self):
        messages.success(self.request, "Logged Out Successfully ")
        return reverse_lazy("home")


def changeProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeProfile(request.POST , instance = request.user)
            if form.is_valid():
                messages.success(request,'Update profile Successfully !')
                form.save()
                return redirect('home')
        else:
             form = ChangeProfile(instance = request.user)
        return render(request,'register.html',{'form':form ,'type':'Chanage profile'})

    else:
        return redirect('login')


def change_pass(request):
    if request.user.is_authenticated:
        if request.method  == 'POST':
            form = PasswordChangeForm(request.user , data = request.POST)
            if form.is_valid():
                messages.success(request,'Password chanage successfuly !')
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('showData')
        else:
            form  = PasswordChangeForm(user = request.user)
        return render(request,'register.html',{'form':form,'type':'Chanage Password'})
    else:
        return redirect('login')

                

         
         