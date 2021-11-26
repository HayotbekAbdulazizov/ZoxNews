from django.db.models.fields import SlugField
from .models import Post, Category,  LikedPosts


def view_all(request):
	try:
		liked_posts = LikedPosts.objects.get(id=request.session['user_liked_posts_id'])
	except:
		liked_posts = LikedPosts.objects.create()
		request.session['user_liked_posts_id'] = liked_posts.id
	print(liked_posts)
	
	context = {
		'liked_news':request.session,
        'categories':Category.objects.all(),
		'liked_posts':liked_posts,
    }
	return context
	
