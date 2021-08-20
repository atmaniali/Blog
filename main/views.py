from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .form import *
from .models import *

# Create your views here.
class home(generic.list.ListView):
    template_name = "main/home.html"
    model = Post

def createpost(request):
    template_name = "main/createpost.html"
    context = {}
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context['form'] = form
    return render(request, template_name, context)

def updatepost(request, post_id):
    # id = 2
    obj = get_object_or_404(Post, pk = post_id)
    context = {}
    form = PostForm(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return reverse("main:home")

    template_name = 'main/modifierpost.html'
    context['form'] = form
    return render(request, template_name, context)
def detail(request, question_id):
    post = get_object_or_404(Post, pk = question_id) 
    return render(request, 'main/chhkl.html', {"post": post})
def profile(request):
    template_name="account/profile.html"
    context={}
    return render(request,template_name, context)    

