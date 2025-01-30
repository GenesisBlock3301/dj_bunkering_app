from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'bunkering', 'concern', 'team', 'career', 'quote', 'contact', 'terms', 'fleet']

    def location(self, item):
        return reverse(item)
