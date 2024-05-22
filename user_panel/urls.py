from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views.dashboard import *
from .views.user.post.posts import *
from .views.user.post.post_create import *
from .views.auth.user_login import user_login
from .views.auth.user_register import user_register
from .views.auth.user_logout import user_logout

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', include('user_panel.views.admin.urls')),
    path('uesr/', include('user_panel.views.user.urls')),

    path('login/', user_login, name='user_panel_login'),
    path('register/', user_register, name='user_panel_register'),
    path('logout/', user_logout, name='user_panel_logout'),
]

