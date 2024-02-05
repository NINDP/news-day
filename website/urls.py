from django.urls import path
from website.views import *

urlpatterns = [
    path('', index, name="home"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('category/<int:id>', index),
    path('news/<int:id>', news_page),
]
