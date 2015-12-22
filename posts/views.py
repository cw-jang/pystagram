from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.core.paginator import Paginator
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .forms import PostForm
from .models import Post
from photos.models import Photo


def list_posts(request):
    page = request.GET.get('page', 1)
    per_page = 5
    posts = Post.objects.order_by('created_at')
    pg = Paginator(posts, per_page)

    try:
        contents = pg.page(page)
    except PageNotAnInteger:
        contents = pg.page(1)
    except EmptyPage:
        contents = []

    for content in contents:
        print('content=', content)
        print('content.photo=', content.photo)

        if content.photo is not None:
            content.thumb_url = content.photo.thumb_url
        else:
            content.thumb_url = ''

    return render(request, 'list_posts.html', {'posts':contents, })


def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    photo_url = ''
    if post.photo is not None:
        photo = Photo.objects.get(pk=post.photo.pk)
        photo_url = photo.image_url

    return render(request, 'view_post.html', {'post':post, 'photo_url':photo_url})


def create_post(request):
    # if pk is not None:
    #     post = get_object_or_404
    #     form = PostForm(instance=post)
    if request.method == 'GET':
        form = PostForm()
        form.photo = Photo.objects.order_by('?').first()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            photo_pk = request.POST.get('photo')
            post.photo = Photo.objects.get(pk=photo_pk)
            post.save()
            return redirect('posts:view_post', pk=post.pk)

    return render(request, 'edit_post.html', 
        {'form':form})


def edit_post(request, pk):
    # FIXME: 기존의 post 내용이 수정되는게 아니라 새로운 post가 생성되는 문제가 있습니다
    if request.method == 'POST':
        return create_post(request)

    else:
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        form.photo = post.photo
    
    return render(request, 'edit_post.html', {'form':form})