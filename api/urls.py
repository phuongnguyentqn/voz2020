from django.urls import path

from api import views

app_name = 'api'
urlpatterns = [
    path('threads/', views.ThreadListView.as_view(), name='thread-list'),
    path('threads/<int:pk>/', views.ThreadDetailView.as_view(), name='thread-detail'),
    path('threads/<int:tid>/posts/', views.PostListView.as_view(), name='post-list'),
]
