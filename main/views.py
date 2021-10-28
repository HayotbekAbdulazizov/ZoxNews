from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Category, Post, LikedPosts
from django.views.generic import DetailView, ListView, UpdateView
import json


# Main Home page
class HomePageView(ListView):
    model = Post
    template_name = 'index.html'

#  For Post details
class PostDetailsView(DetailView):
    model = Post
    template_name  = 'post-details.html'

# Sorting By category
class CategorySortView(DetailView):
    model = Category
    template_name  = 'category-sort.html'

# For Updating Posts
class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = '__all__'
    success_url = '/'


# Init of Liked_Posts model
def liked_posts_init(request):
    try:
        liked_posts = LikedPosts.objects.get(id=request.session.get('user_liked_posts_id'))
    except:
        liked_posts = LikedPosts.objects.create()
        request.session['user_liked_posts_id'] = liked_posts.id	
    return liked_posts



# Like for Posts with AJAX
def add_to_liked(request):
    print(' Function AddLike ')
    d = request.GET.get('data')
    data  = json.loads(d)
    liked_posts = liked_posts_init(request)
    post_id = data['post_id']
    post = Post.objects.get(id=post_id)
    if post.id in liked_posts.liked_posts:
        post.likes -= 1
        liked_posts.liked_posts.remove(post.id)
    else:
        liked_posts.liked_posts.append(post.id)
        post.likes += 1
    liked_posts.save()    
    post.save()

    status = {
        'product_like':post.likes
    }
    return JsonResponse(status)



def add_post(request):

    return render(request, 'index.html')



# FNC for saving Comments With AJAX 
def comment(request):
    name = request.GET.get('name')
    post_slug = request.GET.get('post_slug')
    return redirect(f'/details/{post_slug}')



# https://stackoverflow.com/questions/7786493/convert-string-to-html-code-in-django-template    