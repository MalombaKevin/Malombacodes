from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from malombacodes_app.forms import Post_Form, Profile_Form
from malombacodes_app.models import malombacodes_Post, malombacodes_Profile

# Create your views here.


# @login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')


# @login_required(login_url='/accounts/login/')
def create_profile(request):
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit = False)
            profile.user=request.user
            profile.save()
            return redirect('profile')
    else:
        form=Profile_Form()
    return render(request, 'add/create_profile.html', {'form':form})

# @login_required(login_url='/accounts/login/')
def profile(request):
    if malombacodes_Profile.objects.filter(user_id=request.user.id).exists():
        profile = malombacodes_Profile.objects.get(user_id=request.user.id)
        posts = malombacodes_Post.objects.filter(user_id = request.user.id).all()
        
    else:
        profile = None
        posts= None
    return render(request, 'profile.html')

def create_post(request):
    if request.method == 'POST':
        form = Post_Form(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit = False)
            post.user=request.user
            post.save()
            return redirect('profile')
    else:
        form=Post_Form()
    return render(request, 'add/create_post.html', {'form':form})
    

