from django.contrib import admin
from .models import PostArticle, PostComment


# Register your models here.

@admin.register(PostArticle)
class PostArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'publish')
    list_filter = ('status', 'publish', 'creat', 'author')
    search_fields = ('title', 'PostBody')
    ordering = ('status', 'publish')
    date_hierarchy = ('publish')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)


@admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, requsts, queryset):
        queryset.update(active=True)