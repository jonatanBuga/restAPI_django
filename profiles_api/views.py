from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializer


class HelloApiView(APIView):

    serializer_class = serializer.HelloSerializer
    def get(self,request,format=None):
        an_apiview ={
            'Uses HTTP method as function(get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',

        }
        return Response({'message':'Hello','an_apiview':an_apiview})
    def post(self,request):
        """create Hello message with our name """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message ':message})
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        

class HelloViewSets(viewsets.ViewSet):
    serializer_class = serializer.HelloSerializer
    
    def list(self,request):
        a_viewsets =[
            'uses actions (create, retrive, update,...)',
            'frovides more functionalty with less code'
        ]
        return Response({'message ':'Hello','a_viewsets':a_viewsets})
    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})