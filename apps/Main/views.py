from django.shortcuts import render,redirect, get_object_or_404
from apps.Main.models import *
from django.http import HttpResponseRedirect
from apps.Main.form import UserRegisterForm, PostForm, EditProfileForm
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import tweepy

CONSUMER_KEY = 'VWG7GWaCbKC8NXuoZurBELbMI' #API key
CONSUMER_SECRET = 'WrU8PKpNeJBwgWUoJQ07lD4v9lwDDA9CqnLc7rzXQag0xkCfxH' #API key secret
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAJ6FLwEAAAAADg5%2BufGeft5cGnEJaASFN9LJ0zo%3DO1lkExojNLnjF8rnbQnYjREsDZqQa7JjewB0FiJgxux5ZragHo' #BTOKENEARER 
ACCESS_TOKEN ='447441948-YoTQTzp7ETHEjc8lVce2tmrMNfORG3CPHEdqx1m2' #ACCESTOKEN
ACCESS_TOKEN_SECRET = 'QGlLiljPaKkudccx3wF10LaIkY3PAalr7IXvDGyD64ohG' #ACCESTOKENSECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True,
                    wait_on_rate_limit_notify=True,)

trends_result = api.trends_place(23424982)[:10]

@login_required
def feed(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    posts = Post.objects.all()
    if request.method =='POST':
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.user = current_user
            post.save()
    else:
        formulario = PostForm()
    return render(request, 'social/feed.html', {'posts': posts, 'formulario':formulario, 'trends':trends_result[0]['trends']})

@login_required
def trends(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    posts = Profile.objects.all()
    return render(request, 'social/trends.html', {'posts': posts, 'trends':trends_result[0]['trends']})

@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'social/register.html', context)

@login_required
def profile(request, username=None):
    current_user = request.user
    friends = Profile.objects.all()
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/profile.html', {'user':user, 'posts':posts, 'friends':friends})

@login_required
def notificaciones(request):
    post = Post.objects.all().order_by('?')[:10]
    follow = Relationship.objects.all()
    return render(request, 'social/notificaciones.html', {'post':post, 'follow':follow,'trends':trends_result[0]['trends']})


def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    return redirect('feed')


def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    return redirect('feed')

@login_required
def editarPerfil(request,user_id):
    perfil = Profile.objects.get(id=user_id)
    if request.method =='GET':
        formulario = EditProfileForm(instance=perfil)
    else:
        formulario = EditProfileForm(request.POST,request.FILES, instance=perfil)
        if formulario.is_valid():
            formulario.save()
        return redirect('profile')
    return render(request, 'social/edit_profile.html', {'formulario':formulario})