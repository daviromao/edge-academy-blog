from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from .models import SignUpCode

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            code = request.GET.get('code', None)
            signUpCode = SignUpCode.objects.filter(code=code, email=form.cleaned_data['email']).first()
            if(not signUpCode):
                form.add_error('email', 'Código de cadastro inválido')
                return render(request, 'register.html', {'form': form})
            form.save()
            signUpCode.delete()
            return redirect('myauth:login')
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('blog:index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('blog:index')