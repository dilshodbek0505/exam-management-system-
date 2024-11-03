import random

from django.utils import timezone

from celery import shared_task

from .models import Exam, Test, TestItem



@shared_task
def generate_tests_for_exams():
    exams = Exam.objects.filter(start_time__lte=timezone.now(), end_time__gte=timezone.now())
    
    for exam in exams:
        for student in exam.students.all():

            test, created = Test.objects.get_or_create(
                exam=exam,
                student=student
            )
            
            if created:              
                questions = exam.subject.questions.all()
                selected_questions = random.sample(list(questions), min(exam.question_counts, questions.count()))

                test_items = [ TestItem(test=test,question=question) for question in selected_questions]
                TestItem.objects.bulk_create(test_items)
