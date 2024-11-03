from django.urls import path

from .api_endpoints import *

app_name = 'exam'


urlpatterns = [
    path('subjects/', SubjectListApi.as_view(), name='subjects-list'),
    path('subjects/create/', SubjectCreateApi.as_view(), name='subjects-create'),
    path('subjects/<uuid:pk>/', SubjectDetailsApi.as_view(), name='subject-details'),

    path('exams/', ExamListApi.as_view(), name='exams-list'),
    path('exams/create/', ExamCreateApi.as_view(), name='exams-create'),
    path('exams/<uuid:pk>/', UserExamApi.as_view(), name='user-exam-list'),
    path('exams/details/<uuid:pk>/', ExamDetailsApi.as_view(), name='exam-details'),

    path('tests/<uuid:pk>/',TestRetrieveApi.as_view(), name='test-retrieve'),
    path('tests/<uuid:pk>/submit/', TestAnswerApi.as_view(), name='user-answer-for-test'),
    path('tests/<uuid:pk>/results/', StudentResultApi.as_view(), name='student-result'),
]
