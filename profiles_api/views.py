from rest_framework.views import APIView #we installed the restframework in our requirements.txt
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer  #serializers- a feature of the REST framework allows to confer data inputs into python objects and vice versa
                                                    #|-> it is similar to a form in a standard view-(with HTML)

    def get(self, request, format=None): #format is used to add a format suffix to the end of the endpoint url
        """Returns a list of APIView features"""
        an_apiview = [
                'Uses HTTP methods as functions (get, post, patch, put, delete)',
                'Is similar to a traditional Django View',
                'Gives you the most control over your application logic',
                'Is mapped manually to the URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):  #HTTP put is often used to update an object (generally a specific one, hence the pk)
        """Handle updating an object""" #|->unlike patch it replaces the object with the new one provided
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None): #HTTP patch updates only the fields provided in the request
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})
