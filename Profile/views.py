from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Login.models import User
from Blogs.models import Blog

# Create your views here.
@login_required
def profile_view(request, username):
  if request.method == 'GET':
    profile = get_object_or_404(User, username=username)
    blogs = Blog.objects.filter(author=profile)

    return render(request, 'Profile/profile.html', {'profile': profile, 'blogs': blogs})