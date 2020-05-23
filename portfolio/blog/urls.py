from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<slug:post_slug>/', views.detail_post, name='detail_post')
]