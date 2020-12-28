from rest_framework.views import APIView #we installed the restframework in our requirements.txt
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None): #format is used to add a format suffix to the end of the endpoint url
        """Returns a list of APIView features"""
        an_apiview = [
                'Uses HTTP methods as functions (get, post, patch, put, delete)',
                'Is similar to a traditional Django View',
                'Gives you the most control over your application logic',
                'Is mapped manually to to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
