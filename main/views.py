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

