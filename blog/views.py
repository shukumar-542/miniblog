from django.shortcuts import render,HttpResponseRedirect
from .forms import userForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post

# HOME
def home(request):
      posts= Post.objects.all
      return render(request, 'blog/home.html',{'posts':posts})

# ABOUT
def about(request):
      return render(request, 'blog/about.html')

# CONTACT
def contact(request):
      return render(request, 'blog/contact.html')

# DASHBORD
def dashbord(request):
      posts= Post.objects.all
      return render(request, 'blog/dashboard.html',{'posts':posts})
# LOGIN
def user_login(request):
      if not request.user.is_authenticated:
            if request.method == "POST":
                  form = LoginForm(request=request, data=request.POST)
                  if form.is_valid():
                        uname = form.cleaned_data['username']
                        upass = form.cleaned_data['password']
                        user =authenticate(username = uname, password= upass)
                        if user is not None:
                              login(request,user)
                              messages.success(request, 'Logged in successfully')
                              return HttpResponseRedirect('/dashbord/')
            else:
                  form = LoginForm()
            return render(request, 'blog/login.html',{'form': form})
      else:
            return HttpResponseRedirect('/dashbord/')
# LOGOUT
def user_logout(request):
      logout(request)
      return HttpResponseRedirect('/')
# SIGNUP
def signup(request):
      if request.method == 'POST':
            form = userForm(request.POST)
            if form.is_valid():
                  # messages.success(request,'You Account Created SuccessFully')
                  form.save()
      else:
            form = userForm()

      return render(request, 'blog/signup.html',{'form':form})
def add_post(request):
      if request.user.is_authenticated:
           
                  
            return render(request, 'blog/addpost.html')
      else:
            return HttpResponseRedirect('/login/')

def update_post(request,id):
      if request.user.is_authenticated:
            return render(request, 'blog/updatepost.html')
      else:
            return HttpResponseRedirect('/login/')

def delete_post(request ,id):
      if request.user.is_authenticated:
            return HttpResponseRedirect('/dasboard/')
      else:
            return HttpResponseRedirect('/login/')
