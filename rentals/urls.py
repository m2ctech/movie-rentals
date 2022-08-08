from django.urls import path
from . import views


app_name = 'rentals'


urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies' ),
    path('<int:movie_id>/', views.details, name='details' ),
]