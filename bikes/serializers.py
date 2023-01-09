from rest_framework import serializers
from .models import Manufacturer, Bike, Image, Category

# class ManufacturerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Manufacturer
#         fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)

class BikeSerializer(serializers.ModelSerializer):
    cat = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Bike
        fields = ('images', 'title', 'link', 'first_post', 'cat', 'post_date')

    def get_cat(self, obj):
        return obj.cat.cat
    
    def get_images(self, obj):
        serializer = ImageSerializer(obj.images, many=True)
        images = []
        for image in serializer.data:
            images.append(image['image'])
        return images

