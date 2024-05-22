from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from blog.views.home import home
from .views.categories import categories
from .views.post_details import *
from .views.about_me import about_me


urlpatterns = [
    path('', home , name='blog_home'),
    path('categories/', categories , name='blog_categories'),
    path('about_me/', about_me , name='blog_about_me'),
    path('post/<int:id>/', post_details , name='blog_post_details'),
    path('post/<int:id>/comment/', post_comment , name='blog_post_comment'),
    path('post/<int:post_id>/like/', post_like , name='blog_post_like'),
    path('post/<int:post_id>/<int:comment_id>/', post_reply , name='blog_post_reply'),
    path('post/<int:post_id>/<int:comment_id>/delete/', post_comment_delete , name='blog_post_comment_delete'),
] 
