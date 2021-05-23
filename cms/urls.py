from django.urls import path, re_path
from cms.models import Story
from cms import views

app_name = "cms"
urlpatterns = [
    path('search/', views.search, name="search"),
    path('<slug>/', views.StoryDetail.as_view(), name="storydetail"),
    path('', views.StoryList.as_view(), name="storyhome"),
    path('category/<slug>', views.category, name="category"),  
]
