from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import LoginForm, SignupForm
from .models import User, Avatar

# Create your views here.
def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']

      user = authenticate(username=username, password=password, email=email)
      if user is not None:
        login(request, user)
        return redirect('index')
  else:
    form = LoginForm()
  return render(request, 'Login/login.html', {'form': form})

def signup_view(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password1 = form.cleaned_data['password1']
      password2 = form.cleaned_data['password2']

      if (password1 == password2):
        # Busco usuarios con el mismo username o email
        users = User.objects.filter(Q(username=username) | Q(email=email))

        if (not users):
          # Guardo el usuario con el avatar por defecto
          avatar = Avatar()
          avatar.image = "avatars/default-avatar.jpg"
          avatar.save()

          user = User(username=username, email=email, avatar=avatar)
          user.set_password(password1)
          user.save()
          return redirect('login')

        form.errors['username'] = 'El nombre de usuario o email ya están registrados.'
        return render(request, 'Login/signup.html', {'form': form})

      form.errors['password2'] = 'Las contraseñas ingresadas no coinciden.'
      return render(request, 'Login/signup.html', {'form': form})
  else:
    form = SignupForm()
  return render(request, 'Login/signup.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect('index')