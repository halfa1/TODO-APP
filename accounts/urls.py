from django.urls import path
from .views import register_view,login_view,home_view #logout_view
from django.contrib.auth.views import LogoutView
from todo.views import task_list

urlpatterns = [
    path('',register_view,name='register'),
    path('login/',login_view,name='login'),
    #path('home/',home_view,name='home'),
    path('tasklist',task_list,name='tasklistings'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
]