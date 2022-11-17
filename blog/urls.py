from django.urls import path
from .views import home, single_post



app_name="blog"
urlpatterns = [
path ('', home , name="home"),
path("posts/<int:pk>", single_post , name="single_post")
]

