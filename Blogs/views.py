from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import CreateBlogForm
from .models import Blog
from datetime import datetime

# Create your views here.
def blog_detail_view(request, pk):
  if request.method == 'GET':
    blog = Blog.objects.filter(id=pk)

    if not blog:
      return render(request, 'Index/404.html')

    return render(request, 'Blogs/blogDetail.html', {'blog': blog[0]})

@login_required
def create_blog_view(request):
  if request.method == 'POST':
    form = CreateBlogForm(request.POST, request.FILES)
    if form.is_valid():
      title = form.cleaned_data['title']
      subtitle = form.cleaned_data['subtitle']
      image = form.cleaned_data['image']
      date = datetime.today().strftime('%Y-%m-%d')
      author = request.user

      blog = Blog(title=title, subtitle=subtitle, image=image, date=date, author=author)
      blog.save()
      return redirect('index')
  else:
    form = CreateBlogForm()
  return render(request, 'Blogs/createBlog.html', {'form': form})

@login_required
def delete_blog(request, pk):
  if request.method == 'DELETE':
    blog = get_object_or_404(Blog, id=pk)

    if (blog.author == request.user) or (request.user.is_staff):
      blog.delete()
      return redirect('index')

    raise PermissionDenied()