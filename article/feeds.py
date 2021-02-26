from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import PostArticle

class LatestPostsFeed(Feed):
    title = 'SiteMat8'
    link = reverse_lazy('article:postarticle')
    description = 'New posts of SiteMat8.'

    def items(self):
        return PostArticle.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.PostBody, 30)