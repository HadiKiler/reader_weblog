from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .users.users import users
from .users.user_create import user_create
from .users.user_edit import user_edit
from .users.user_delete import user_delete

from .categories.categories import categories
from .categories.category_edit import category_edit
from .categories.category_delete import category_delete

from .tags.tags import tags
from .tags.tag_edit import tag_edit
from .tags.tag_delete import tag_delete

from .posts.posts import posts
from .posts.post_edit import post_edit
from .posts.post_delete import post_delete

from .comments.comments import comments
from .comments.comment_show import comment_show

from .likes.likes import likes

urlpatterns = [
    path('users', users, name="user_panel_admin_users"),
    path('user/create/', user_create, name="user_panel_admin_user_create"),
    path('user/<int:id>/edit/', user_edit, name="user_panel_admin_user_edit"),
    path('user/<int:id>/delete/', user_delete, name="user_panel_admin_user_delete"),

    path('categories/', categories, name="user_panel_admin_categories"),
    path('category/<int:id>/edit/', category_edit, name="user_panel_admin_category_edit"),
    path('category/<int:id>/delete/', category_delete, name="user_panel_admin_category_delete"),

    path('tags/', tags, name="user_panel_admin_tags"),
    path('tags/<int:id>/edit/', tag_edit, name="user_panel_admin_tag_edit"),
    path('tags/<int:id>/delete/', tag_delete, name="user_panel_admin_tag_delete"),

    path('posts/', posts, name="user_panel_admin_posts"),
    path('posts/<int:id>/edit/', post_edit, name="user_panel_admin_post_edit"),
    path('posts/<int:id>/delete/', post_delete, name="user_panel_admin_post_delete"),

    path('comments/', comments , name="user_panel_admin_comments"),
    path('comment/<int:id>/show/', comment_show , name="user_panel_admin_comment_show"),

    path('likes/', likes , name="user_panel_admin_likes"),
    
]
