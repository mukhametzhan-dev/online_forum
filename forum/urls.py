from django.urls import path
from views import post_list, post_detail, post_create, post_update, post_delete

urlpatterns = [
    path('', post_list, name='post-list'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('post/new/', post_create, name='post-create'),
    path('post/<int:pk>/edit/', post_update, name='post-update'),
    path('post/<int:pk>/delete/', post_delete, name='post-delete'),
]
