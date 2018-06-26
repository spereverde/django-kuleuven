from rest_framework import serializers
from .models import Post, Person, Unit

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ('nr', 'firstName', 'lastName')

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit