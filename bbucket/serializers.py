from rest_framework import serializers
from .models import Bucket

class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bucket
        fields = ('id', 'owner', 'name', 'visited','desc', 'created_at', 'updated_at')