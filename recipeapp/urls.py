from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.recipe_create, name='recipe_add'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:id>/edit/', views.recipe_update, name='recipe_edit'),
     path('recipe/<int:id>/delete/', views.recipe_delete, name='recipe_delete'),
]

