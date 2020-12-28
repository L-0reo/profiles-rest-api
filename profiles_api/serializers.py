from rest_framework import serializers

class HelloSerializer(serializers.Serializer): #serializers- a feature of the REST framework allows to confer data inputs into python objects and vice versa
    """Serializes a name field for testing our APIView"""   #|-> it is similar to a form in a standard view-(with HTML)
    name = serializers.CharField(max_length=10)
