from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name="blog"
urlpatterns = [
path ('/', views.home , name="home"),
path("posts/", views.mainposts , name="posts"),
path("posts/<int:pk>/", views.single_post , name="singlepost"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

