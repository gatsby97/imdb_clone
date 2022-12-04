from django.urls import path,include
#from watchmate.api.views import movie_list,movie_detail
from watchmate.api.views import WatchListAV, WatchDetailAV,StreamPlatformListAV,StreamPlatformDetailAV,ReviewListAV,ReviewDetailAV,ReviewCreateAV

# in class based views class name is passed with as_view() method
urlpatterns = [
    path('list/', WatchListAV.as_view(), name= 'movie-list'),       
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream',StreamPlatformListAV.as_view(), name = 'streamplatform-list'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name = 'streamplatform-detail'),
    path('stream/<int:pk>/review-create',ReviewCreateAV.as_view(),name='review-list'),
    path('stream/<int:pk>/reviews',ReviewListAV.as_view(),name='review-list'),
    path('stream/reviews/<int:pk>',ReviewDetailAV.as_view(),name='review-detail'),
    #path('reviews',ReviewListAV.as_view(), name='review-list'),
    #path('reviews/<int:pk>',ReviewDetailAV.as_view(),name='review-detail')
    
    ]