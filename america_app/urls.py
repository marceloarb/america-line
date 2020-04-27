from django.urls import path
from . import views	

urlpatterns = [
    path('',views.index_login),
    path('homepage',views.homepage),
    path('create_user', views.create_user),
    path('login', views.login),
    path("add_favorite", views.add_favorite),
    path('remove_favorite',views.remove_favorite),
    path('delete_session', views.delete_session),
    path('favorites', views.view_favs),
    path('remove_favorite_homepage',views.remove_favorite_homepage),
    path('new_release',views.new_release),
    path('action',views.action),
    path('drama',views.drama),
    path('comedy',views.comedy),
    path('planair', views.planair),
    path('register', views.register),
]