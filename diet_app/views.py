from django.shortcuts import render
from diet_app.models import *
from diet_app.serializers import *
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,RetrieveUpdateAPIView,ListAPIView,DestroyAPIView
from django.contrib.auth import backends
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from diet_app.permissions import IsOwner
from diet_app.utility_func import calculate_bmr
# Create your views here.
class SignupView(CreateAPIView):
    serializer_class=UserSerializer
class ProfileView(CreateAPIView):
    serializer_class=UserProfileSeriaizer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user_object=self.request.user
        # data=serializer.validated_data
        # bmr=calculate_bmr(
        #     age=data.get('age'),
        #     height=data.get('height'),
        #     weight=data.get('weight'),
        #     gender=data.get('gender'),
        #     activity_level=data.get('activity_level')
                        
                                    
        # )
        return serializer.save(owner=user_object)
class ProfileRetrieveView(RetrieveAPIView,UpdateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    serializer_class=UserProfileSeriaizer
    queryset=UserProfile.objects.all()


class UserRetriveView(RetrieveAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    serializer_class=UserSerializer
    queryset=CustomUser.objects.all()

class UserProfileRetriveView(RetrieveAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    serializer_class=CombinedUserProfileSerializer
    queryset=CustomUser.objects.all()

class FoodLogCreateView(CreateAPIView,ListAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=FoodlogSerializer
    queryset=Foodlog.objects.all()

    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class FoodLogRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    serializer_class=FoodlogSerializer
    queryset=Foodlog.objects.all()

 