from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name="login"),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('prof_delete/<email>', views.prof_delete, name="prof_delete"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('prof_update/<email>', views.prof_update, name="prof_update"),

]