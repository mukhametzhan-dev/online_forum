from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'forum/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'forum/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content, author=request.user)
        return redirect('post-detail', pk=post.pk)
    return render(request, 'forum/post_form.html')

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden()
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post-detail', pk=post.pk)
    return render(request, 'forum/post_form.html', {'post': post})
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden()
    if request.method == 'POST':
            post.delete()
            return redirect('post-list')
    return render(request, 'forum/post_confirm_delete.html', {'post': post})