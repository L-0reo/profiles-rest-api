from django.urls import path

from profiles_api import views

urlpatterns = [
path('hello-view/', views.HelloApiView.as_view()), #as_view is the standard function to convert our APIView class to be rendered by URLs
]
