from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student
from django.contrib.auth import authenticate


class StudentSerializer(serializers.ModelSerializer):
      class Meta:
            model = Student
            fields = ['user', 'image', 'phone_no', 'account_no', 'slug']

class RegistrationSerializer(serializers.ModelSerializer):
      confirm_password = serializers.CharField(required=True)
      class Meta:
            model = User
            fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
            
      def save(self):
            username = self.validated_data['username']
            first_name = self.validated_data['first_name']
            last_name = self.validated_data['last_name']
            email = self.validated_data['email']
            password = self.validated_data['password']
            password2 = self.validated_data['confirm_password']
            
            if password != password2:
                  raise serializers.ValidationError({'error': 'Password does not match'})
            if User.objects.filter(email = email).exists():
                  raise serializers.ValidationError({'error': 'Email already exists'})
            if User.objects.filter(username=username).exists():
                  raise serializers.ValidationError({'error': 'Username already exists'})
            
            account = User(username=username, first_name=first_name, last_name=last_name, email=email)
            account.set_password(password)
            account.is_active = False
            account.save()
            return account
      
class LoginSerializer(serializers.Serializer):
      email = serializers.EmailField(required=True)
      password = serializers.CharField(required=True)
            
      def validate(self, data):
            email = data.get('email')
            password = data.get('password')
            
            if email and password:
                  user = authenticate(email = email, password = password)
            
                  if not user:
                        raise serializers.ValidationError('Invalid email or password')
                  
                  if not user.is_active:
                        raise serializers.ValidationError('User account is not active')
            else:
                  raise serializers.ValidationError('Both email and password are required')
            
            return data
            