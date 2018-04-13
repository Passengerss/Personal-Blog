from django.conf.urls import url
from . import views

urlpatterns=[
    url(r"^movie_service/(\d+)",view=views.movie_source,name="movie_service"),
]