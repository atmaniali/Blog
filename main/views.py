from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .form import *
from .models import *

# Create your views here.
class home(generic.list.ListView):
    template_name = "home.html"
    model = Post

def createpost(request):
    template_name = "createpost.html"
    context = {}
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context['form'] = form
    return render(request,template_name,context)

# def updatepost(request, pk):
    # id = 2
    obj = Post.objects.get(id = pk)
    context = {}
    form = PostForm(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return reverse("main:home")

    template_name = 'modifierpost.html'
    context['form'] = form
    return render(request, template_name, context)
####
# 
def updatechek(request, pk):
    template_name = 'chhkl.html'
    context = {}
    post = Post.objects.get(id = pk)
    form = PostForm(request.POST or None, instance= post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('main:home')
    context['form'] = forms
    return render(request, template_name, context)    

