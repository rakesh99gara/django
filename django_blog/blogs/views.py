from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from blogs.models import Post,Comment,Tag
from blogs.forms import PostForm,CommentForm,TagForm,CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    latest_posts = Post.objects.all().order_by('-id')
    paginator = Paginator(latest_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Tag.objects.all()
    context = {
        'posts': page_obj,
        'tags':tags,
        'head' : "Recent Posts"
    }
    return render(request, 'blogs/index.html', context)

@login_required(login_url='login')
def newPost(request):
    form = PostForm()
    tag_form = TagForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        tag_form = TagForm(request.POST)
        if form.is_valid() and tag_form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            tags = tag_form.cleaned_data['tag']
            for i in tags.split(','):
                tag = Tag.objects.get_or_create(tag=i)[0]
                post.tags.add(tag)
            return redirect('showPost',post.id)
    context = {'form':form,'tag_form':tag_form,'form_title':'Create New Post','btn':'Create Post'}
    return render(request,'blogs/new.html',context)

def showPost(request,postid):
    post = Post.objects.get(pk = postid)
    comments = post.comment_set.all()
    comment_form = CommentForm()
    tags = post.tags.all()
    context = {
        'post' : post,
        'comments' : comments,
        'comment_form' : comment_form,
        'tags':tags
    }
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.name = request.user
            comment.post = post
            comment_form.save()
    return render(request, 'blogs/show.html', context)


def editPost(request,postid):
    post = Post.objects.get(pk=postid)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('showPost',postid)
    context = {'form':form,'form_title':'Edit Post','btn':'Edit Post'}
    return render(request,'blogs/new.html',context)


def deletePost(request,postid):
    Post.objects.get(pk=postid).delete()
    # context = {}
    return redirect('index')

def deleteComment(request,postid,commentid):
    Comment.objects.get(pk=commentid).delete()
    return redirect('showPost',postid)

def tagPosts(request,tagid):
    tag = Tag.objects.get(id=tagid)
    posts = tag.posts.all().order_by('-id')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    tags = Tag.objects.all()
    context = {
        'posts' : page_obj,
        'tags':tags,
        'head' : "Posts on "+tag.tag
    }
    return render(request,'blogs/index.html',context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account Created for "+user)
            return redirect('login')
    context = {'form':form}
    return render(request,'registration/register.html', context )    

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Username or Password is incorrect")
    context = {}
    return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')





# Create your views here.
