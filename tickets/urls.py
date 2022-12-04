from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_query', views.review_query, name='my_query')
]