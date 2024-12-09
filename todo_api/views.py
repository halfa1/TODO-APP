from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import User, Task, Tag
from .serializers import UserSerializer,TaskSerializer, TagSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self,request, *args, **kwargs):
        instance = self.get_object()
        #soft delete ie change a record column
        #instance.description = "deleted"
        #instance.save()

        #or hard delete
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TagViewSet(viewsets.ModelViewSet):
    queryset =Tag.objects.all()
    serializer_class = TagSerializer