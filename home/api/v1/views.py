from django.http import HttpResponse
from .serializers import TaskSer
from rest_framework import viewsets
from home.models import Task
from .pagination import CustomPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    pagination_class = CustomPagination
   # filter_backends = 
    search_fields = ['title']
    ordering_fields = ['created_date']
    filterset_fields = ['complete']

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.queryset
    #     serializer = TaskSer(queryset, many=True)
    #     return Response(serializer.data)
