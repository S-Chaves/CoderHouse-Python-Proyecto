from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Login.models import User, Avatar
from Blogs.models import Blog
from .forms import EditProfileForm

# Create your views here.
@login_required
def profile_view(request, username):
  if request.method == 'GET':
    profile = get_object_or_404(User, username=username)
    blogs = Blog.objects.filter(author=profile)

    return render(request, 'Profile/profile.html', {'profile': profile, 'blogs': blogs})

@login_required
def edit_profile_view(request):
  if request.method == 'POST':
    form = EditProfileForm(request.POST, request.FILES)
    if form.is_valid():
      avatar = form.cleaned_data['avatar']
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      description = form.cleaned_data['description']
      web_page = form.cleaned_data['web_page']

      user = User.objects.get(id=request.user.id)
      # Chequeo que el email elegido no esté tomado
      if User.objects.filter(Q(email=email) & ~Q(email=user.email)):
        form = default_form(request)
        form.errors['email'] = 'El email ya está registrado.'
        return render(request, 'Profile/editProfile.html', {'form': form})

      user.name = name
      user.description = description
      user.email = email
      user.web_page = web_page

      # Si cargó un avatar elimino el anterior y guardo el nuevo
      if avatar:
        old_avatar = Avatar.objects.get(id=user.avatar.id)
        old_avatar.delete()
        new_avatar = Avatar()
        new_avatar.image = avatar
        new_avatar.save()
        user.avatar =  new_avatar

      user.save()
      return redirect('profile', username=user.username)
  else:
    form = default_form(request)
  return render(request, 'Profile/editProfile.html', {'form': form})

def default_form(request):
  return EditProfileForm(initial={
      'email': request.user.email,
      'description': request.user.description,
      'avatar': request.user.avatar,
      'name': request.user.name,
      'web_page': request.user.web_page
    })