from rest_framework import serializers
from diet_app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","username","email","password","phone"]
        read_only_fields=["id"]
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
class UserProfileSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields="__all__"
        read_only_fields=["id","bmr","owner"]

class CombinedUserProfileSerializer (serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password','phone','profile']
        read_only_fields=['id']
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    def get_profile(self, obj):
        profile_obj= UserProfile.objects.get(owner=obj)
        serializer_instance=UserProfileSeriaizer(profile_obj)
        return serializer_instance.data

class FoodlogSerializer(serializers.ModelSerializer):
    class Meta:
          model=Foodlog
          fields="__all__"
          read_only_fields=["id","owner","created_at"]
