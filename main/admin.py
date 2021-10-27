from django.contrib import admin
from .models import Post, Category, LikedPosts, Comment, Tags 
# Register your models here.

admin.site.register(LikedPosts)

# Registering Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']


# Registering Tag model
@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}

#  Registering main Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'id']
	list_display_links = ['title', 'id' ]
	prepopulated_fields = {'slug':('title',)}

	
# Registering Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}
