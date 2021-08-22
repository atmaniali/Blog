from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_variables
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from .form import *
from .models import *

# Create your views here.
class home(generic.list.ListView):
    template_name = "main/home.html"
    model = Post

@login_required
def createpost(request):
    template_name = "main/createpost.html"
    context = {}
    # TODO: fix user by the one how's connect
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context['form'] = form
    return render(request, template_name, context)

@login_required
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
    # tags for security
@sensitive_variables('user')    
def profile(request, user_id):
    template_name="account/profile.html"
    user = User.objects.get(pk=user_id)
    users = User.objects.all().select_related('profile')    
    context={"users":users}
    if user.is_authenticated:
       post = Post.objects.all().filter(user = user_id)
       context['posts'] = post
    return render(request,template_name, context)   

def settings_profile(request):
    template_name = "account/settings.html"
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return reverse('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context['user_form'] = user_form
        context['profile_form'] = profile_form
    # TODO: add the avatar and test if they work    
    return render(request, template_name, context)

# 

def friendship_request(request):
    other_user = User.objects.get(pk=3)
    Friend.objects.add_friend(
        request.user,                               # The sender
        other_user,                                 # The recipient
        message='Hi! I would like to add you')      # This message is optional
    return HttpResponse('request was sent to {}'.format(other_user.username))


