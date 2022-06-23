from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from malombacodes_app.forms import Profile_Form

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
