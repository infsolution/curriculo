from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id','username','password','email')



class CandidateSerializer(serializers.HyperlinkedModelSerializer):
	usuario = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	class Meta:
		model = Candidate
		fields = ('url', 'id', 'name', 'usuario', 'address')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
	usuario = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
	class Meta:
		model = Company
		fields = ('url', 'id', 'name', 'usuario')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
	candidate = CandidateSerializer()
	#candidate = serializers.SlugRelatedField(queryset=Candidate.objects.all(), slug_field='usuario')
	class Meta:
		model = Address
		fields = ('url', 'id', 'candidate', 'street', 'number', 'district', 'city', 'state', 'country', 'zip_code')