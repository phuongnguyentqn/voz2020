from django.urls import path

from api import views

app_name = 'api'
urlpatterns = [
    path('threads/', views.ThreadListView.as_view(), name='thread-list'),
    path('threads/(?P<pk>[0-9]+)/', views.ThreadDetailView.as_view(), name='thread-detail'),
    path('threads/(?P<tid>[0-9]+)/posts/', views.PostListView.as_view(), name='post-list'),
]
