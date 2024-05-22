from django.contrib import admin
from django.urls import path,include
from .api.user import *
from .api.category import *
from .api.tag import *
from .api.post import *
from .api.comment import *
from .api.Like import *
from .api.login import *

urlpatterns = [
    path('admin/login', login ),
    
    path('user', UserViewSet.as_view({'get': "list", 'post': 'create'})),
    path('user/<int:id>', UserViewSet.as_view({'get': "retrieve", 'put': "update", 'delete': "destroy"})),
    
    path('category', CategoryViewSet.as_view({'get': "list", 'post': 'create'})),
    path('category/<int:id>', CategoryViewSet.as_view({'get': "retrieve", 'put': "update", 'delete': "destroy"})),

    path('tag', TagViewSet.as_view({'get': "list", 'post': 'create'})),
    path('tag/<int:id>', TagViewSet.as_view({'get': "retrieve", 'put': "update", 'delete': "destroy"})),

    path('post', PostViewSet.as_view({'get': "list", 'post': 'create'})),
    path('post/<int:id>', PostViewSet.as_view({'get': "retrieve", 'put': "update", 'delete': "destroy"})),
    
    path('comment', CommentViewSet.as_view({'get': "list", 'post': 'create'})),
    path('comment/<int:id>', CommentViewSet.as_view({'get': "retrieve", 'put': "update", 'delete': "destroy"})),

    path('like', LikeViewSet.as_view({'get': "list", 'post': 'create'})),
    path('like/<int:id>', LikeViewSet.as_view({'get': "retrieve", 'put': "update", 'delete': "destroy"})),
]
