from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, toggle_publish, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', never_cache(PostListView.as_view()), name='post_list'),
    path('blog/<slug:slug>/', cache_page(60)(PostDetailView.as_view()), name='post_item'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('blog/update/<slug:slug>/', never_cache(PostUpdateView.as_view()), name='post_update'),
    path('blog/delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    path('blog/toggle/<slug:slug>/', toggle_publish, name='toggle_publish')

]