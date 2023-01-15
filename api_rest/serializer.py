from rest_framework import serializers
from . models import Tribe,Ministry,Red,Membership,Users

class TribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribe
        fields = ('id','name','charge','created_at','update_at')
        read_only_fields = ('created_at','update_at')

class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ('id','name','charge','created_at','update_at')
        read_only_fields = ('created_at','update_at')   

class RedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Red
        fields = ('id','name','charge','created_at','update_at')
        read_only_fields = ('created_at','update_at')


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('id','name','surname_paternal','surname_maternal','age','email','date_of_birth','red','ministry','tribe','created_at','update_at')
        read_only_fields = ('created_at','update_at')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','user_name','password','membership','created_at','update_at')
        read_only_fields = ('created_at','update_at')