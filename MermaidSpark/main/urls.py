from django.urls import path, re_path
from .views.frontend_view import  index


urlpatterns=[
    path('', index,name ="index"),

]