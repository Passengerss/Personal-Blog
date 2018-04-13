from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(\d+)/',view=views.show,name="show_book"),
    url(r'^edit/(\d+)',views.edit,name="edit"),
    url(r'edit_handle/(\d+)',views.edit_handle,name="edit_handle"),
    url(r"^add/",views.add,name="add"),
    url(r"^add_handle/(\d+)",views.add_handle,name="add_handle"),
    url(r"^delete/(\d+)",views.delete,name="delete"),
]