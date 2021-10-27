from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

# Category Model
class Category(models.Model):
	name = models.CharField('Category name', max_length=100)
	slug = models.SlugField("*", max_length=100, unique=True)

	def __str__(self):
		return f"{self.name}"


# Tag Model 
class Tags(models.Model):
	name = models.CharField('Tag name', max_length=100)
	slug = models.SlugField("*", max_length=100, unique=True)

	def __str__(self):
		return f"{self.name}"
 

 #  Main Post model
class Post(models.Model):
	title = models.CharField("Title", max_length=300, blank=True)
	slug = models.SlugField("*", max_length=300, unique=True, blank=True)
	image = models.ImageField("Poster", upload_to='posters/', blank=True)
	image_local = models.URLField(max_length=200, blank=True)
	author = models.CharField("Author", max_length=100, blank=True)
	body = models.TextField("body", blank=True)
	rich_body = RichTextField()
	published = models.DateTimeField(auto_now_add=True)
	views = models.PositiveIntegerField("Views", default=0)
	likes = models.PositiveIntegerField('Like', default=0 , blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
	tag = models.ManyToManyField(Tags,)
	source = models.URLField(max_length=200)
	
	def __str__(self):
		return f"{self.title}"

	class Meta:
		ordering = ["-published",]
		verbose_name_plural = 'Posts'



# Model of Comment
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField("Name", max_length=50)
	email = models.EmailField("Email", max_length=250)
	subject = models.CharField("Subject", max_length=100)
	message = models.TextField("Your Text",)

	def __str__(self):
		return f"{self.name}"

	class Meta:
		verbose_name='Comments'
		verbose_name_plural='Comments'


#  To Save Liked Posts Of The USER
class LikedPosts(models.Model):
	liked_posts = []
	
	def __str__(self):
		return f"Liked {self.id}"
