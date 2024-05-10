from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from blog.forms import PostForm
from blog.models import Post


def blog_index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})
    
def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404('Post not found')
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:index')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})