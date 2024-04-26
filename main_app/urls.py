from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('finches/<int:finch_id>/assoc_diet/<int:diet_id>/', views.assoc_diet, name='assoc_diet'),
    path('finches/<int:finch_id>/unassoc_diet/<int:diet_id>/', views.unassoc_diet, name='unassoc_diet'),
    path('diets/', views.DietList.as_view(), name='diets_index'),
    path('diets/<int:pk>/', views.DietDetail.as_view(), name='diets_detail'),
    path('diets/create/', views.DietCreate.as_view(), name='diets_create'),
    path('diets/<int:pk>/update/', views.DietUpdate.as_view(), name='diets_update'),
    path('diets/<int:pk>/delete/', views.DietDelete.as_view(), name='diets_delete'),
]