from django.urls import path
from author.views import register, user_login,profile, user_logout, change_password, set_password, my_blogs, UserLoginView
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/',profile, name="profile"),
    path('logout/',user_logout, name="logout"),
    path('change_pass/',change_password, name="change_pass"),
    path('set_pass/',set_password, name="set_pass"),
    path('my_blogs/',my_blogs, name="my_blogs")
]

