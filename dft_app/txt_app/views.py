from django.http import HttpResponse
from .models import User, Message
from .serializers import MessageViewSerializer, MessageSerializer
from rest_framework import viewsets, filters, status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


def index(request):
    response = """<html><body><p>This is the main page of the Text App.</p><br>
    It's a simple RESTful API for creating and reading
    text messages.</body></html>"""
    return HttpResponse(response)


class MessageViewSet(generics.GenericAPIView):
    serializer_class = MessageViewSerializer
    queryset = Message.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, num):
        '''
        Message view by its ID - returns content and view conter for a message,
        part for which authentication is not needed. URL: /message=<int>.
        This endpoint incements message view value.
        '''
        message = Message.objects.get(pk=num)
        serializer = MessageViewSerializer(message)
        message.view_counter += 1
        message.save()
        return Response(serializer.data)


class MessageChangeViewSet(viewsets.ModelViewSet):
    '''Post/Patch/Delete - create/edit/remove the message'''
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

    # if request.method == 'PATCH':
    #     message = Message.objects.get(pk=request.data['id'])
    #     message.view_counter == 0
    #     message.save()


    #
    # def perform_create(self, serializer):
    #     serializer.save(view_counter==0)


    def patch(self, request):
        message = Message.objects.get(pk=request.data['id'])
        request_values = request.data
        request_values['view_counter'] = 0
        print(request_values)

#        print(message.view_counter)
# TODO: set counter to 0 when editing message
        serializer = MessageSerializer(data=request_values)
#        message.view_counter == 0
#        print(message.view_counter)
        if serializer.is_valid():
            # serializer.data['view_counter'] == 0
            # serializer.view_counter == 0
# #            message.save()
#             serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        serializer = MessageSerializer(Message.objects.get(
                     pk=request.data['id']), data=request.data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
