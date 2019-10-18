from django.conf.urls import url
from my_app import views


urlpatterns = [
    url('page', views.search_page),
    url('search', views.search),
]
