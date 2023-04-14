from django.urls import path

from . import views

app_name = 'league'
urlpatterns = [
    path('', views.leagues, name='leagues'),
    path('<int:league_id>/', views.infoLeague, name='league'),
    path('match/<int:match_id>', views.infoMatch, name='match')
]