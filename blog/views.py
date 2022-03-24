from django.shortcuts import render,HttpResponseRedirect
from .forms import userForm,LoginForm,postForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group

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
                  messages.success(request,'You Account Created SuccessFully')
                  user = form.save()
                  group = Group.objects.get(name ='Author')
                  user.groups.add(group)
      else:
            form = userForm()

      return render(request, 'blog/signup.html',{'form':form})
def add_post(request):
      if request.user.is_authenticated:
            if request.method == 'POST':
                  form = postForm(request.POST)
                  if form.is_valid():
                        form.save()
                        form = postForm()
            else:
                  form = postForm()
           
                  
            return render(request, 'blog/addpost.html',{'form':form})
      else:
            return HttpResponseRedirect('/login/')

def update_post(request,id):
      if request.user.is_authenticated:
            if request.method == "POST":
                  pi= Post.objects.get(pk=id)
                  pst =postForm(request.POST, instance=pi)
                  if pst.is_valid():
                        pst.save()
                        pst = postForm()
            else:
                  pi= Post.objects.get(pk=id)
                  pst =postForm(instance=pi)

            return render(request, 'blog/updatepost.html',{'form': pst})
      else:
            return HttpResponseRedirect('/login/')

def delete_post(request ,id):
      if request.user.is_authenticated:
            if request.method == 'POST':
                  pst = Post.objects.get(pk=id)
                  pst.delete()
            return HttpResponseRedirect('/dashbord/')
      else:
            return HttpResponseRedirect('/login/')
