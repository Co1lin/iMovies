from django.urls import path

from . import views

''' http://ip:port/ '''
''' path('path/', views.method, name = 'name') '''
app_name = 'movies'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('index/', views.index, name = 'index'),
    path('movies/', views.IndexView.as_view(), name='index'),
    path('actors/', views.ActorView.as_view(), name='actors'),
    path('comments/', views.CommentView.as_view(), name='comments'),

    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie'),
    path('actor/<int:pk>/', views.ActorDetailView.as_view(), name='actor'),

    #path('search/', views.SearchView.as_view(), name='search'),
    path('search/', views.search, name='search')
]