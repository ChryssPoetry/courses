from rest_framework import serializers
from .models import course

class CourseSerializer(serializers.ModelSerializer):
	class meta:
		model = course
		fields = ('id','name', 'language', 'price' )