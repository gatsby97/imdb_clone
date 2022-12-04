from rest_framework import serializers
from watchmate.models import WatchList, StreamPlatform, Review

# normal serializers uses models instances importing it as serializer fields 
# special definition of create-update is required 
# in create method validated_data is to check if data passed by client is valid or not 
# in update instance of already present instance is used and updated with validated data
# validation is done by three methods validation by name , validation by all and validators like passed in name below
""" def name_length(value):
    if len(value)<2:
        raise serializers.ValidationError("Name is too short")
    

class MovieSerializer(serializers.Serializer):            
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description =serializers.CharField()
    active = serializers.BooleanField()
    
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
    
    def validate_name(self, value):
        
        if len(value)<2:
            raise serializers.ValidationError("Name is too shot")
        return value
    
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description can't be same")
        return data
        
     """
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
    
class WatchListSerializer(serializers.ModelSerializer): #Model serializer doesn;t need to define create-update methods
    #main meta class is defined import Model mentioning which fields you want
    # if you want all fields just mention '__all__' , exclude to exclude particular fields and fields to get particulare fields
        
    #len_name = serializers.SerializerMethodField() # this is to add field in out json wihtout adding it in models
    
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__"
    
"""     def get_len_name(self, object):
        length = len(object.name)
        return length    
    def validate_name(self, value):
        
        if len(value)<2:
            raise serializers.ValidationError("Name is too shot")
        return value
    
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description can't be same")
        return data """
    
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer): 
    watchlist  = WatchListSerializer(many=True,read_only=True) #Nested Serializers 
    #watchlist = serializers.HyperlinkedRelatedField(many=True,read_only =True,view_name='movie-detail')

    class Meta:
        model = StreamPlatform
        fields = "__all__"
        

        
        

   