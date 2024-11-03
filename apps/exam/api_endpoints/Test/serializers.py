from rest_framework import serializers

from apps.exam.models import Test, TestItem, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answers')


class TestItemSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = TestItem
        fields = ('id', 'question')
    
class TestSerializer(serializers.ModelSerializer):
    items = TestItemSerializer(many=True)
    class Meta:
        model = Test
        fields = ('id', 'percentage', 'items')

class TestAnswerSerializer(serializers.Serializer):
    answer = serializers.CharField(max_length = 1)
