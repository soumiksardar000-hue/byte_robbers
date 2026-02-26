
from django.urls import path

from . import views

app_name = "complains"


urlpatterns=[
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('like/',views.like_post, name='like_post'),
    

]