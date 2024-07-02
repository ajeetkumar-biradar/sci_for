from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    id = serializers.IntegerField(required=False)  # Not required for POST requests
    title = serializers.CharField(max_length=200)
    body = serializers.CharField()
