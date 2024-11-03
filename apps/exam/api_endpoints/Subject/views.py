from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import SubjectSerializer
from apps.exam.models import Subject


class SubjectListApi(ListAPIView):
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Subject.objects.all()
    pagination_class = None



class SubjectCreateApi(CreateAPIView):
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Subject.objects.all()


class SubjectDetailsApi(RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Subject.objects.all()
    http_method_names = ['patch', 'delete']


__all__ = [
    'SubjectListApi',
    'SubjectCreateApi',
    'SubjectDetailsApi'
]
