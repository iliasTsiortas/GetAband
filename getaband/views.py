from .models import User
from .serializers import UserSerializer
from rest_framework import generics

from django.contrib.staticfiles import views


def index(request, path=''):
    if path.endswith('.js'):
        return views.serve(request,path)
    else:
        return views.serve(request, 'index.html')


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):

        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username__contains =username)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
