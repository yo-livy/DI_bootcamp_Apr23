from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from .models import Image

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('my_images')  # Replace 'my_images' with your desired URL name for the user's uploaded images page
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def view_images(request):
    images = Image.objects.all()
    return render(request, 'view_images.html', {'images': images})

@login_required
def my_images(request):
    images = Image.objects.filter(user=request.user)
    total_images = request.user.profile.total_images
    return render(request, 'my_images.html', {'images': images, 'total_images': total_images})


