from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from rest_framework import validators
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Customer, Product, Order

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({'passwords': 'Passwords must match'})

        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        return user

class CustomerSerializer(serializers.ModelSerializer):
    user  = UserSerializer(required=True)
    class Meta:
        model = Customer
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(),validated_data=user_data)
        customer = Customer(user=user,Total_payble_amount = validated_data.pop('Total_payble_amount'),is_vendor = validated_data.pop('is_vendor'))
        customer.save()

        return customer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'