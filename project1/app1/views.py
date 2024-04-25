from django.shortcuts import render,redirect
from django.views import View
from app1.forms import LoginForm,BlogForm,EditForm
from django.contrib.auth import authenticate,login
from app1.models import Blog
from django.views.generic import UpdateView
from django.urls import reverse_lazy


# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'index.html',{'form':form})

    def post(self,request,*args,**kwargs):
        uname=request.POST['username']
        pswd=request.POST['password']
        user=authenticate(request,username=uname,password=pswd)
        if user:
            login(request,user)
            return redirect('home_view')
        else:
            return redirect('log_view')
        
class CreateBlog(View):
    def get(self,request,*args,**kwargs):
        form=BlogForm()
        return render(request,'createblog.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        title=request.POST['title']
        content=request.POST['content']
        author=request.POST['author']
        image=request.POST['image']
        Blog.objects.create(title=title,content=content,author=author,image=image)
        return redirect('home_view')

class ListBlog(View):
    def get(self,request,*args,**kwargs):
        data=Blog.objects.all()
        return render(request,'listblog.html',{'data':data})

class EditBlog(UpdateView):
    model=Blog
    template_name='editblog.html'
    pk_url_kwarg='id'
    form_class=EditForm
    context_object_name='form'
    success_url=reverse_lazy('list_view')

class DeleteBlog(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        data=Blog.objects.get(id=id)
        data.delete()
        return redirect('list_view')