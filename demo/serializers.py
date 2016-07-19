# coding:utf-8

from rest_framework import serializers
from models import Message,UserMessage

class MessageSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    class Meta:
        model =  Message

class UserMessageSerializer(serializers.ModelSerializer):
    MessageSerializer = MessageSerializer
    class Meta:
        model = UserMessage
        depth = 2
    
    
    
    
    
    
    
    
                                    
    
    
   
    


