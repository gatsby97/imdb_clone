from django.contrib import admin
from watchmate.models import WatchList,StreamPlatform,Review #Movie

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)