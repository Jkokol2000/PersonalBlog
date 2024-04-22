from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='display_post'),
    path("post/<int:pk>/" , views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>', views.delete_post, name='delete_post')
]