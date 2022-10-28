from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    
    path('', views.Index.as_view(), name="index"), #トップページへのURL
    path("list", views.SaunaList.as_view(), name="list"),
    path("form", views.Sauna_form.as_view(), name = "form"),
    path('detail/<int:pk>/',views.Sauna_Detail.as_view(),name='detail'), 
    path('update/<int:pk>',login_required(views.Sauna_update.as_view()),name='update'), 
    path('delete/<int:pk>',login_required(views.Sauna_delete.as_view()),name='delete'), 
    path('signup/',views.Signup.as_view(),name='signup'),
    path('', include("django.contrib.auth.urls")),
    path('mypage/',login_required(views.MypageView.as_view()),name='mypage'),
    

]