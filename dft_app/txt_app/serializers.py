from rest_framework import serializers
from .models import Message


class MessageViewSerializer(serializers.ModelSerializer):
    '''For unauthenticated views'''

    class Meta:
        model = Message
        fields = ('content', 'view_counter')


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
