from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

#class based view looks for a template 
app_name='blog'

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home' ),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts' ),    
    #to create routes which for each post this mean we need a variable to this route
    # pk : post key
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail' ),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update' ),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete' ),
    path('post/new/', PostCreateView.as_view(), name='post-create' ),
    path('about/', views.about, name='blog-about' ),
]
