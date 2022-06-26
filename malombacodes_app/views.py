from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from malombacodes_app.forms import Meme_Form, Post_Form, Profile_Form
from malombacodes_app.models import Memes, malombacodes_Post, malombacodes_Profile

# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    posts = malombacodes_Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit = False)
            profile.user=request.user
            profile.save()
            return redirect('/')
    else:
        form=Profile_Form()
    return render(request, 'add/create_profile.html', {'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    if malombacodes_Profile.objects.filter(user_id=request.user.id).exists():
        profile = malombacodes_Profile.objects.get(user_id=request.user.id)
        posts = malombacodes_Post.objects.filter(user_id = request.user.id).all()
        
        
    else:
        profile = None
        posts= None
    return render(request, 'profile.html', {'profile': profile, 'posts':posts})

@login_required(login_url='/accounts/login/')
def create_post(request):
    if request.method == 'POST':
        form = Post_Form(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit = False)
            post.user=request.user
            post.save()
            return redirect('/')
    else:
        form=Post_Form()
    return render(request, 'add/create_post.html', {'form':form})

@login_required(login_url='/accounts/login/')
def create_meme(request):
    if request.method == 'POST':
        form = Meme_Form(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit = False)
            post.user=request.user
            post.save()
            return redirect('/memes')
    else:
        form=Meme_Form()
    return render(request, 'add/create_meme.html', {'form':form})

@login_required(login_url='/accounts/login/')
def memes(request):
    memes = Memes.objects.all()
    return render(request, 'm&m/memes.html', {'memes': memes})

@login_required(login_url='/accounts/login/')
def all_users(request):
    profiles=malombacodes_Profile.objects.all()
    return render(request, 'all-users.html', {'profiles': profiles})

def user(request,id):
    if malombacodes_Profile.objects.filter(user_id=id).exists():
        profile = malombacodes_Profile.objects.get(user_id=id)
        posts = malombacodes_Post.objects.filter(user_id =id).all()
        
        
    else:
        profile = None
        posts= None
    return render(request, 'user.html', {'profile': profile, 'posts':posts})
