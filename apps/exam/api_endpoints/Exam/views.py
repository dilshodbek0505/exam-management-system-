from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ExamSerializer

from apps.exam.models import Exam



class ExamCreateApi(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class ExamListApi(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ExamSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Exam.objects.all()
        else:
            
            return Exam.objects.filter(students__in = [self.request.user])
        
    def get_serializer(self, *args, **kwargs):
        
        kwargs['fields'] = ['id', 'title', 'description']

        return super().get_serializer(*args, **kwargs)

class UserExamApi(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ExamSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Exam.objects.filter(students__in = [self.request.user], pk=self.kwargs[self.lookup_field])

    def get_serializer(self, *args, **kwargs):
        
        kwargs['fields'] = ['id', 'title', 'description', 'start_time', 'end_time', 'question_counts', 'subject', 'pass_percentage']

        return super().get_serializer(*args, **kwargs)
    
class ExamDetailsApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ExamSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Exam.objects.all()
    http_method_names = ['patch', 'get', 'delete']
    lookup_field = 'pk'
    

__all__ = [
    'ExamCreateApi',
    'ExamListApi',
    'UserExamApi',
    'ExamDetailsApi'
]

