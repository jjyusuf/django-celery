from __future__ import absolute_import, unicode_literals

from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response

from .serializers import CommentSerializer
from myapp.tasks import send_email

class CommentView(views.APIView):

    def get(self, request):
        return Response("Please post a comment", status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            send_email.delay(serializer.validated_data['email'], serializer.validated_data['subject'], serializer.validated_data['message'])
            return Response({'message':'Email sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
