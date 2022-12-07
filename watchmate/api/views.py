from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,viewsets
from rest_framework.exceptions import ValidationError
#from rest_framework import mixins
#from rest_framework.decorators import api_view
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from watchmate.api.serializers import (WatchListSerializer,
                                    StreamPlatformSerializer,
                                    ReviewSerializer) #replace Movieserializer with updated WatchListSerializer
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
""" class ReviewDetailAV(mixins.RetrieveModelMixin,generics.GenericAPIView):
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
        return self.create(request,*args,**kwargs) """

class ReviewCreateAV(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        movie= WatchList.objects.get(pk=pk)
        reviewer = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie,reviewer=reviewer)
        if review_queryset.exists():
            raise ValidationError("User has already reviewed this")
        serializer.save(watchlist=movie,reviewer=reviewer)
        

class ReviewListAV(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)
    
    
  
class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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
    
class StreamPlatformAV(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

""" class StreamPlatformAV(viewsets.ViewSet):# no need to make 2 diff urls for these two classes 
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True,context={'request':request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        stream = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(stream,context={'request':request})
        return Response(serializer.data)
    
    def create(self, request):
        serializer = StreamPlatformSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) """

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
    


