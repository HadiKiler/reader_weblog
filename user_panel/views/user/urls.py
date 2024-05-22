from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .post.posts import posts
from .post.post_create import post_create
from .post.post_edit import post_edit
from .post.post_delete import post_delete
from .profile.profile import profile

urlpatterns = [
    path('posts/', posts , name='user_panel_user_posts'),
    path('post/create/', post_create , name='user_panel_user_post_create'),
    path('post/<int:id>/edit/', post_edit , name='user_panel_user_post_edit'),
    path('post/<int:id>/delete/', post_delete , name='user_panel_user_post_delete'),

    path('profile/', profile , name='user_panel_user_profile'),
]
