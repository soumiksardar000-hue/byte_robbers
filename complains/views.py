from django.shortcuts import get_object_or_404, redirect, render

from complains.models import Complain, Category, Like
from django.db.models import Q

# Create your views here.
def posts_by_category(request , category_id):
    posts= Complain.objects.filter(complain_status='Undone',category=category_id)
    
    try:

        category=Category.objects.get(pk=category_id)
    except:
        return redirect('home')
        
    context = {
        'posts':posts,
        'category':category,
    }
    return render(request , 'posts_by_category.html', context)

# Create your views here.
def blogs(request , slug):
    single_blog = get_object_or_404(Complain,slug=slug)
    
    context={
        'single_blog':single_blog,
        

    }
    return render(request , 'blogs.html',context)



def search(request):

    keyword = request.GET.get('keyword')

    complains = None

    if keyword:

        complains = Complain.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(complain_body__icontains=keyword),
            complain_status='Undone'
        )

    context = {
        'complains': complains,
        'keyword': keyword,
    }

    return render(request, "search.html", context)


# ✅ Fix your complain_view
def complain_view(request):
    featured_posts = Complain.objects.filter(complain_status='Undone').order_by('-created_at')[:3]
    posts = Complain.objects.filter(complain_status='Done').order_by('-created_at')

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'user': request.user,
    }
    return render(request, 'home.html', context)


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Complain.objects.get(id=post_id)


        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like,created =Like.objects.get_or_create(user=user,post_id=post_id)


        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect(request.META.get('HTTP_REFERER', 'hackathon_main:home'))