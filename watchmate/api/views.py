from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
#from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from watchmate.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer #replace Movieserializer with updated WatchListSerializer
# Create your views here.
from rest_framework.views import APIView
from watchmate.models import WatchList,StreamPlatform,Review # Movies models is replaced with watchlist serializer 


# views are of 2 types class based and function based views 
# function based views decorators api_view is used and methods are defined using if else conditions like "GET,POST"etc
#
"""
@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer  = MovieSerializer(movie,many= True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def movie_detail(request,pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error: movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    """
class ReviewDetailAV(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self, request , *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    
       
    

class ReviewListAV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request , *args, **kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

class WatchListAV(APIView):
    
    # in class based views have their inbuilt methods like get, post, delete delete etc but we have to pass serializer and return response
    # here movies data is used to display with serializer.data
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many= True)
        return Response(serializer.data)
        
    # we need to check passed data with request.data if it is valid or not and then we save it and return response with serializer data     
        
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        
class WatchDetailAV(APIView):
    # status object to pass status codes from status clss from DRF
    def get(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error: movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
            
        
    def put(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors)
      
    def delete(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformListAV(APIView):
    
    def get(self,request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True,context = {'request':request})#passed to HyperlinkedModelSerializer ,context={'request':request})
        return Response(serializer.data)        
          
    def post(self, request):
        serializer = StreamPlatformSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class StreamPlatformDetailAV(APIView):
    
    def get(self,request,pk):
        #platform_detail = StreamPlatform.objects.get(pk=pk)
        try:
            platform_detail= StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'stream paltform not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform_detail,context = {'request':request})
        return Response(serializer.data)
    def put(self,request,pk):
        platform_detail = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform_detail,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        deleted_obj = StreamPlatform.objects.get(pk=pk)
        deleted_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

