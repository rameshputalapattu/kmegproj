from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='kmeg-home'),
    path('upload/', views.upload_page, name='kmeg-upload'),
    path('<int:image_id>/image', views.image, name='image'),
    path('<int:image_id>/kmegimage', views.kmegimage, name='kmegimage')

]
