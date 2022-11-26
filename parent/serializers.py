from rest_framework import serializers
from .models import Parentinfo

class ParentSerializer(serializers.ModelSerializer):
    # image=serializers.ImageField()
    # contact=serializers.IntegerField()
    class Meta:
        model=Parentinfo
        fields=['name','child','address','contact','image']

