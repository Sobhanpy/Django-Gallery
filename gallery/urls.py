from django.urls import path
from .views import *

app_name = 'gallery'

urlpatterns = [
    path("gallery-detail/<int:id>/", gallery_information, name="gallery-informations"),
    path("category/<str:cat>",gallery ,name ="gallery-category"),

]