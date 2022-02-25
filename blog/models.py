from django.db import models
from accounts.models import Account
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,
							unique_for_date='publish')
	author = models.ForeignKey(Account,
							   on_delete=models.CASCADE,
							   related_name='blog_posts')
	body = RichTextUploadingField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,
							  choices=STATUS_CHOICES,
							  default='draft')
	featured_image = models.ImageField(upload_to='images/%Y/%m/%d/')
	objects = models.Manager()  # The default manager.
	published = PublishedManager()  # Our custom manager.
	post_views = models.IntegerField(default=0, null=True, blank=True)
	tags = TaggableManager()
	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail',
					   args=[self.publish.year,
							 self.publish.month,
							 self.publish.day,
							 self.slug])

        

class TeamAbout(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)


class About(models.Model):
    about_1 = models.CharField(max_length=1000)
    about_2 = models.CharField(max_length=1000)
    about_2 = models.CharField(max_length=1000)
    team = models.ForeignKey(TeamAbout, on_delete=models.CASCADE, null=True)
    
    
class Contact(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	name = models.CharField(verbose_name="Name", max_length=100)
	email = models.EmailField(verbose_name="Email", max_length=100, blank=True)
	subject = models.CharField(verbose_name="Subject", max_length=255)
	message = models.TextField(verbose_name="Message")

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name_plural = 'Contact'
		verbose_name = 'Contact'
		ordering = ["timestamp"]
