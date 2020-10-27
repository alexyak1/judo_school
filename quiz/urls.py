from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('<int:techniques_id>/', views.detail, name='detail'),
    path('<int:techniques_id>/vote/', views.vote, name='vote'),
]