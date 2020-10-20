from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),

    path('<int:techniques_id>/', views.detail, name='detail'),
    path('<int:techniques_id>/results/', views.results, name = 'results'),
    path('<int:techniques_id>/vote/', views.vote, name='vote'),
]