from django.shortcuts import get_object_or_404, redirect, render
from .forms import AddUserForm, BlogPostForm, CategoryForm, EditUserForm

from django.template.defaultfilters import slugify
from complains.models import Category , Complain
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Complain.objects.all().count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)


def categories(request):
    return render(request, 'dashboard/categories.html')

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)


def posts(request):
    posts = Complain.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)

# ✅ FIXED
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # ✅ Set slug BEFORE saving, not after
            post.slug = slugify(post.title)
            post.save()
            # If slug needs the ID to be unique, fix it now
            post.slug = slugify(post.title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
        else:
            print(form.errors)
    else:
        form = BlogPostForm()

    context = {'form': form}
    return render(request, 'dashboard/add_post.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Complain, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'dashboard/edit_post.html', context)

def delete_post(request, pk):
    post = get_object_or_404(Complain, pk=pk)
    post.delete()
    return redirect('posts')
