from django.shortcuts import render
from Blogs.models import Blog

# Create your views here.
def index_view(request):
  if request.method == 'GET':
    blogs = Blog.objects.all()
    return render(request, 'Index/index.html', {'blogs': blogs, 'user': request.user})

def page_not_found(request, exception):
  return render(request, "Index/404.html")

def page_forbidden(request, exception):
  return render(request, "Index/403.html")
