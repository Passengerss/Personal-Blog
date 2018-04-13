from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^index/",view=views.index,name="index"),
    url(r"^register/",views.register,name="register"),
    url(r"^register_handle/",views.register_handle,name="register_handle"),
    url(r"^register_exist/(\w+)",views.register_exist,name="register_exist"),
    url(r"^login/",views.login,name="login"),
    url(r"^loginout/",views.loginout,name="loginout"),
    url(r'^login_handle/',views.login_handle,name="login_handle"),
    url(r"^user_center/",views.user_center,name="user_center"),
    url(r"^update_info/",views.update_info,name="update_info"),
]