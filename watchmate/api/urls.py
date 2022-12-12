from django.urls import path,include
from rest_framework.routers import DefaultRouter
#from watchmate.api.views import movie_list,movie_detail
from watchmate.api.views import WatchListAV,StreamPlatformAV, WatchDetailAV,StreamPlatformListAV,StreamPlatformDetailAV,ReviewListAV,ReviewDetailAV,ReviewCreateAV


router = DefaultRouter()
router.register('stream', StreamPlatformAV,basename='streamplatform')
# in class based views class name is passed with as_view() method
urlpatterns = [
    path('list/', WatchListAV.as_view(), name= 'movie-list'),       
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    path('',include(router.urls)),
    #path('stream',StreamPlatformListAV.as_view(), name = 'streamplatform-list'),
    #path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name = 'streamplatform-detail'),
    path('<int:pk>/review-create',ReviewCreateAV.as_view(),name='review-create'),
    path('<int:pk>/reviews',ReviewListAV.as_view(),name='review-list'),
    path('review/<int:pk>',ReviewDetailAV.as_view(),name='review-detail'),
    #path('reviews',ReviewListAV.as_view(), name='review-list'),
    #path('reviews/<int:pk>',ReviewDetailAV.as_view(),name='review-detail')
    
    ]