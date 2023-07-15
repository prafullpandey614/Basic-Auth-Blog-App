from . import views
from django.urls import path

urlpatterns = [

    path('',views.APIOverview.as_view()),
    path('register',views.RegisterAPIView.as_view()),
    path('login',views.LoginAPIView.as_view(),name='login'),
    path('logout',views.LogoutAPIView.as_view()),
    path('home',views.HomePage.as_view()),
    path('add-blog',views.AddBlogAPIView.as_view()),
    path('update-blog',views.UpdateBlogAPIView.as_view()),
]
