from django.contrib.sitemaps import Sitemap
from .models import PostArticle


class PostSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.9

    def items(self):
        return PostArticle.published.all()

    def lastmod(self, obj):
        return obj.update