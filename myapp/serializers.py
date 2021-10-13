from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=500)

