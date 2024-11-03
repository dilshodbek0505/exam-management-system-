from rest_framework import serializers

from apps.exam.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'name_ru', 'name_uz')
        extra_kwargs = {
            'name_ru': {'write_only': True},
            'name_uz': {'write_only': True},
        }
    


