from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    image = serializers.CharField(max_length=255)


    def create (self, validate_data):
        return Books.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
