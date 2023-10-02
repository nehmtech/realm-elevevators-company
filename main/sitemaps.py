from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['about', 'services', 'projects', 'contact', 'quote']

    def location(self, item):
        return reverse(item)

class AppViewSitemap(Sitemap):
    def items(self):
        return ['app_development', 'broadcasting',  'data_analysis',
                'database_development', 'digital_marketing', 'graphic_design',
                'it_consultancy', 'it_hardware_configuration', 'networking',
                'online_writing', 'photography', 'software_development',
                'videography', 'web_development']

    def location(self, item):
        return reverse(item)

class LegalViewSitemap(Sitemap):
    def items(self):
        return ['terms_and_conditions', 'privacy_policy']

    def location(self, item):
        return reverse(item)

class PostsSitemap(Sitemap):
    def items(self):
        return ['latest_posts']

    def location(self, item):
        return reverse(item)

