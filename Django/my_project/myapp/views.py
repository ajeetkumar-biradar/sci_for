# myapp/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer  # Ensure this line correctly imports PostSerializer
import requests


class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        if response.status_code == 200:
            return response.json()
        return []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=request.data)
        try:
            response_data = response.json()
        except ValueError:
            return Response({"detail": "Error parsing JSON response from the external API"},
                            status=response.status_code)
        return Response(response_data, status=response.status_code)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'pk'

    def get_object(self):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{pk}')
        if response.status_code == 200:
            return response.json()
        return None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{pk}', json=request.data)
        try:
            response_data = response.json()
        except ValueError:
            return Response({"detail": "Error parsing JSON response from the external API"},
                            status=response.status_code)
        return Response(response_data, status=response.status_code)

    def partial_update(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{pk}', json=request.data)
        try:
            response_data = response.json()
        except ValueError:
            return Response({"detail": "Error parsing JSON response from the external API"},
                            status=response.status_code)
        return Response(response_data, status=response.status_code)

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pk}')
        if response.status_code == 200:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Error deleting the resource from the external API"}, status=response.status_code)
