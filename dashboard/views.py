from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Project, Message
from .forms import ProjectForm, MessageForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# View for the login page
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})

# View for the signup page
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/signup.html', {'form': form})

# View for the dashboard
def dashboard(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(user=request.user)  
        return render(request, 'dashboard/dashboard.html', {'projects': projects})
    else:
        return redirect('login')

# View for creating a project
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'dashboard/create_project.html', {'form': form})

# View for editing a project
def edit_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dashboard/edit_project.html', {'form': form, 'project': project})

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'dashboard/inbox.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  
            message.save()

            return redirect('inbox')  
    else:
        form = MessageForm()

    return render(request, 'dashboard/send_message.html', {'form': form})

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if message.receiver == request.user:
        message.delete()
        return redirect('inbox')  
    else:
        return redirect('inbox')  

def logout_view(request):
    logout(request)  
    return redirect('login')  
