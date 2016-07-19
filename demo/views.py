# coding:utf-8
from rest_framework import generics
from models import Message,UserMessage
import serializers

class MessageCreateListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer

class UserMessageListView(generics.ListCreateAPIView):
    queryset = UserMessage.objects.all()
    serializer_class = serializers.UserMessageSerializer


    








