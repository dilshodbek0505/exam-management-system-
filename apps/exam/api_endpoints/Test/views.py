from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.exam.models import Test, TestItem
from .serializers import TestSerializer, TestAnswerSerializer



class TestRetrieveApi(RetrieveAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsAuthenticated, )


class TestAnswerApi(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TestAnswerSerializer
    
    def get_queryset(self):   
        try:
            return TestItem.objects.get(pk = self.kwargs['pk'])
        except TestItem.DoesNotExist:
            return None
            

    def post(self, requets, *args, **kwargs):
        serializer = self.serializer_class(data = self.request.data)
        serializer.is_valid(raise_exception=True)

        user_answer = serializer.validated_data['answer']
        test = self.get_queryset()
    
        if test is None:
            return Response({'not found'}, status=200)
    
        
        if user_answer == test.question.correct_answer:
            test.is_ture = True
            test.save()
        
        return Response({'success'}, status=200)

class StudentResultApi(APIView):
    permission_classes = (IsAuthenticated,)    
    
    def get_queryset(self, pk):
        try:
            return Test.objects.get(pk = pk)
        except Test.DoesNotExist:
            return None

    def calculate_test_statistics(self, test):
        test_items = test.items.all()
        print(test_items)
        correct_count = test_items.filter(is_true=True).count()
        total_questions = test_items.count()
        wrong_count = total_questions - correct_count
    
        percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0
        is_pass = percentage >= test.exam.pass_percentage
        
        test.correct_answers_count = correct_count
        test.wrong_answers_count = wrong_count
        test.percentage = percentage
        test.is_pass = is_pass
        test.save()
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        print(pk)

        test = self.get_queryset(pk)
        print(test)

        if test is None:
            return Response({'not found'},status=404)
        
        print('nondan ')

        if test.student != request.user:
            return Response({'not permissions'}, status=400)
        print('studentdan ham,')
        self.calculate_test_statistics(test)

        return Response({
            "correct_answers_count": test.correct_answers_count,
            "wrong_answers_count": test.wrong_answers_count,
            "percentage": test.percentage,
            "is_pass": test.is_pass,
        })
        
        
        


__all__ = [
    'TestRetrieveApi',
    'TestAnswerApi',
    'StudentResultApi',
]

