from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
# from .forms import ContactForm, SearchForm
from taggit.models import Tag
from django.db.models import Count
from django.db.models import Q
from django.views import generic
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


# class ContactView(generic.FormView):
#     template_name = "blog/contact.html"
#     form_class = ContactForm
#     success_url = "/contact"

#     def form_valid(self, form):
#         form.save()
#         messages.success(self.request, 'Thanks for contacting us!')
#         return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html')



# search view
# def post_search(request):
#     form = SearchForm
#     results = []

#     if 'q' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             q = form.cleaned_data['q']

#             results = Post.objects.filter(title__contains=q)

#     return render(request, 'blog/search.html', {'form': form, 'results': results})


class PostList(ListView):
    model = Post
    # paginate_by = 2
    queryset = Post.published.all()
    context_object_name = "posts"
    template_name = "blog/blog-list.html"

def blog(request, tag_slug=None):
    posts = Post.published.all()

    # post tag
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 9)  # 5 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/blog-list.html', {'posts': posts, page: 'pages', 'tag': tag})


class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/blog-single.html"

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]
    post.post_views = post.post_views + 1
    post.save()

    return render(request,
                    'blog/blog-single.html',
                    {'post': post,
                    'similar_posts': similar_posts})