from django.urls import path
from posts.views import feeds, comment_add, post_add

urlpatterns = [
    path("feeds/", feeds),
    path("comment_add/", comment_add),
    path("post_add/", post_add),
]