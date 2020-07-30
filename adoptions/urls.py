from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adoptions/<int:pet_id>/', views.pet_detail, name='pet_detail')
]
