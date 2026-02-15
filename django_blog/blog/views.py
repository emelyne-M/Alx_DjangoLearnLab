from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .forms import RegistrationForm, PostForm
from .models import Post

# ------------------------
# Authentication Views
# ------------------------

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('home')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

# ------------------------
# Profile View
# ------------------------

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

# ------------------------
# Blog Views
# ------------------------

def home(request):
    latest_posts = Post.objects.order_by('-published_date')[:5]  # latest 5 posts
    return render(request, 'blog/home.html', {'posts': latest_posts})

def posts(request):
    all_posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts': all_posts})

# ------------------------
# Post Management
# ------------------------

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('posts')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def update_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id, author=request.user)  # only author can edit
    except Post.DoesNotExist:
        messages.error(request, "Post not found or you are not allowed to edit it.")
        return redirect('posts')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('posts')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/update_post.html', {'form': form})
