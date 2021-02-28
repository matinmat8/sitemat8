from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class PostArticle(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Posts')
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=250, unique_for_date='publish')
    PostBody = models.TextField()
    creat = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    publish = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    likes = models.ManyToManyField(User, related_name='like_post')

    tags = TaggableManager()

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'{self.title}, {self.PostBody}, {self.tags}'

    def get_absolute_url(self):
        return reverse('article:post_detail',
                       kwargs={"id":self.id})

    def number_of_likes(self):
        return self.likes.count()

class PostComment(models.Model):
    post = models.ForeignKey(PostArticle, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=65)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['active', 'created_on']

    def __str__(self):
        return 'Comment {}'.format(self.body, self.name)


