from rest_framework import serializers

from apps.exam.models import Exam
from apps.exam.api_endpoints.Subject.serializers import SubjectSerializer

from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class ExamSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'title', 'title_ru', 'title_uz', 'description', 'description_ru', 'description_uz', 'question_counts', 'start_time', 'end_time', 'students', 'subject', 'pass_percentage') 
        extra_kwargs = {
            'title_ru': {'write_only': True},
            'title_uz': {'write_only': True},
            'description_ru': {'write_only': True},
            'description_uz': {'write_only': True},
        }
