from django.urls import path

from . import views

app_name = 'list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('increase', views.increase, name='increase'),
    path('decrease', views.decrease, name='decrease'),
]