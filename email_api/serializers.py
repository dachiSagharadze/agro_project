from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255, min_length=12)
    message = serializers.CharField(min_length=12)