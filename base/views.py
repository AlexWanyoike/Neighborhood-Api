from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from django.http import response
from .models import *
from .serializers import *
from .permissions import IsAdminOrReadOnly
from django.http import JsonResponse
from rest_framework import generics
from rest_framework import filters
from django.core.files.storage import default_storage
#from django.contrib.auth.decorators import login_required.
# Create your views here.
class NeighborhoodList(APIView):
  serializer_class=NeighborhoodSerializer
  # permission_classes = (IsAdminOrReadOnly,)

  def get_neighborhood(self, pk):
    try:
        return Neighborhood.objects.get(pk=pk)
    except Neighborhood.DoesNotExist:
        return Http404()

  def get(self,request,format=None):
    neighborhood= Neighborhood.objects.all()
    serializers=NeighborhoodSerializer(neighborhood, many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=NeighborhoodSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      neighborhood=serializers.data
      response = {
        'data': {
            'neighborhood': dict(neighborhood),
            'status': 'success',
            'message': 'neighborhood created successfully',
        }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors , status= status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    neighborhood = self.get_neighborhood(pk)
    serializers = NeighborhoodSerializer(neighborhood, request.data)
    if serializers.is_valid():
      serializers.save()
      neighborhood=serializers.data
      response = {
          'data': {
              'neighborhood': dict(neighborhood),
              'status': 'success',
              'message': 'neighborhood updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    neighborhood = self.get_neighborhood(pk)
    neighborhood.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessList(APIView):
  serializer_class=BusinessSerializer    
  def get_business(self, pk):
    try:
        return Business.objects.get(pk=pk)
    except Business.DoesNotExist:
        return Http404()

  def get(self, request,format=None):
    business=Business.objects.all()
    serializers=BusinessSerializer(business, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers=BusinessSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      business=serializers.data
      response = {
          'data': {
              'business': dict(business),
              'status': 'success',
              'message': 'business created successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    business = self.get_business(pk)
    serializers = BusinessSerializer(business, request.data)
    if serializers.is_valid():
      serializers.save()
      business_list=serializers.data
      response = {
          'data': {
              'business': dict(business_list),
              'status': 'success',
              'message': 'business updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    business = self.get_business(pk)
    business.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
  serializer_class = UserSerializer  

  def get_users(self,pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404()

  def get(self,request,format=None):
    users=User.objects.all()
    serializers=UserSerializer(users, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers=UserSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      users=serializers.data
      response={
        'data':{
          'users':dict(users),
          'status':'success',
          'message':'user created successfully',
        }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self,request,pk,format=None):
    users=self.get_users(pk)
    serializers=UserSerializer(users,request.data)
    if serializers.is_valid():
      serializers.save()
      users_list=serializers.data
      response = {
          'data': {
              'users': dict(users_list),
              'status': 'success',
              'message': 'user updated successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk,format=None):
    users=self.get_users(pk)
    users.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class PostList(APIView):
  serializer_class=PostSerializer

  def get_post(self, pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      raise Http404()

  def get(self,request,format=None):
    post=Post.objects.all()
    serializers=UserSerializer(post, many=True)
    return Response(serializers.data)
  
  def post(self, request,format=None):
    serializers = PostSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      post = serializers.data
      response={
        'data':{
          'post':dict(post),
          'status':'success',
          'message':'Post created successfully',
        }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, format=None):
    post = self.get_post(pk)
    serializers = PostSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      post_list=serializers.data
      response = {
        'data': {
            'post': dict(post_list),
            'status': 'success',
            'message': 'Post updated successfully',
        }
      }
      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    post = self.get_post(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['uploadedFile']
#     file_name = default_storage.save(file.name,file)

#     return JsonResponse(file_name,safe=False)