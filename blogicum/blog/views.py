from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone

from .models import Post, Category
from .module import NUM_POSTS_LIST


def get_posts():
    return Post.objects.all().select_related(
        'author',
        'location',
        'category'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by(
        '-pub_date'
    )


def index(request):
    post_list = get_posts()[:NUM_POSTS_LIST]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(get_posts(), pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug__contains=category_slug
    )
    post_list = get_list_or_404(get_posts(), category_id__exact=category.pk)
    context = {
        'post_list': post_list,
        'category': category
    }
    return render(
        request,
        'blog/category.html',
        context
    )
