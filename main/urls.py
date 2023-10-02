from django.urls import path
from .views import (
    blogs, detail, posts, create_post, latest_posts, search_result,
 about, services, projects, contact, quote, app_development, broadcasting, 
 cyber_security,data_analysis,database_development, digital_marketing,
  graphic_design, terms_and_conditions, privacy_policy, it_consultancy,
   it_hardware_configuration, networking, online_writing, photography,
    software_development, software_development, videography, web_development,
     it_consultancy, detail, posts, search_result, create_post, latest_posts, 
     main
)

from django.views.generic import TemplateView
from forms.views import (contact_success,contact_form, success,ContactFormView)

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, AppViewSitemap, LegalViewSitemap, PostsSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'app': AppViewSitemap,
    'legal': LegalViewSitemap,
    'posts': PostsSitemap
}







urlpatterns = [
    path("blogs/", blogs, name="blogs"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("search", search_result, name="search_result"),


    path("contact_success", contact_success, name="contact_success"),
    path("contact_form", contact_form, name="contact_form"),
    path('success/', success, name='success'),
    path('contact_main_form/', ContactFormView.as_view(), name='contact_main_form'),
    
    
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),   


    # ============== Main pages URL patterns ============ #

    path('', main, name="main"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),
    path('projects/', projects, name="projects"),
    path('contact/', contact, name="contact"),
    path('quote/', quote, name="quote"),
    path('app_development/', app_development, name="app_development"),
    path('broadcasting/', broadcasting, name="broadcasting"),
    path('cyber_security/', cyber_security, name="cyber_Security"),
    path('data_analysis/', data_analysis, name="data_analysis"),
    path('database_development/', database_development, name="database_development"),
    path('digital_marketing/', digital_marketing, name="digital_marketing"),
    path('graphic_design/', graphic_design, name="graphic_design"),
    path('privacy_policy/', privacy_policy, name="privacy_policy"),
    path('terms_and_conditions/', terms_and_conditions, name="terms_and_conditions"),    
    path('it_consultancy/', it_consultancy, name="it_consultancy"),
    path('it_hardware_configuration/', it_hardware_configuration, name="it_hardware_configuration"),
    path('networking/', networking, name="networking"),
    path('online_writing/', online_writing, name="online_writing"),
    path('photography/', photography, name="photography"),
    path('software_development/', software_development, name="software_development"),
    path('videography/', videography, name="videography"),
    path('web_development/', web_development, name="web_development"),
    
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]



