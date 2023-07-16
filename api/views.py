from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status , generics,views, response

from api.serializers import BlogSerializer
from .models import Blog, UserProfile
from django.contrib.auth import authenticate , login,logout

from django.contrib.auth.mixins import LoginRequiredMixin


class APIOverview(views.APIView):
    def get(self,request):
        data = {
            "api/register/" : "Register a New Account",
            "api/login/" : "Log in to your account",
            "api/logout/" : "Log out from your account"
        }
        return response.Response(data)

class RegisterAPIView(views.APIView):
    
    def post(self,request):
        username = request.data['username']
        tagline = request.data['tagline']
        password = request.data['password']

        try:
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.save()
            emp = UserProfile.objects.create(user=user,bio=tagline)
            return response.Response({'Message' : 'Successfully Registered!'},status=status.HTTP_200_OK)
        except :
            return response.Response({'Message' : 'Could not register, Something Went wrong!'},status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPIView(views.APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return response.Response({'Message' : 'Successfully Logged in'},status=status.HTTP_200_OK)
        else:
            return response.Response({'Message' : 'Could not Login, Something Went wrong!'},status=status.HTTP_400_BAD_REQUEST)
        
class LogoutAPIView(views.APIView):
    def post(self,request):
        logout(request)
        return response.Response({"Message":"Logged Out Successfully"})
    
class HomePage(LoginRequiredMixin, views.APIView):
    login_url = '/api/login'
    permission_denied_message = "Please login."

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            data = {
                "Username": request.user.username,
                "Bio": user_profile.bio
            }
            return response.Response(data)
        except UserProfile.DoesNotExist:
            return response.Response({"message": "User profile not found."})

class AddBlogAPIView(LoginRequiredMixin,generics.CreateAPIView):
    model = Blog
    serializer_class = BlogSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class UpdateBlogAPIView(LoginRequiredMixin,generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'
    
class DeleteBlogAPIView(LoginRequiredMixin,generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'

class BlogsListAPIView(LoginRequiredMixin,generics.ListAPIView):
    serializer_class = BlogSerializer
    def get_queryset(self):
        queryset = Blog.objects.filter(author=self.request.user.id)
        print(self.request.user.id)
        return queryset

class MyProfileAPIView(LoginRequiredMixin,views.APIView):
    def get(self,request):
        res = {
            "username" : request.user.username
        }
        return response.Response(res)
    
#added by Gaurav
#second comment by gaurav
#front 432 changes