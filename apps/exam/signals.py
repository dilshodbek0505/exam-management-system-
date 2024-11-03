from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from .models import Subject, Question, Test, TestItem

@receiver(post_save, sender=Subject)
def add_questions_for_new_subject(sender, instance, created, **kwargs):
    if created:        
        questions = []
        for i in range(100):
    
            question_text = f"Test question {i + 1} for {instance.name}"
            answers = [
                {"A": "Option A"},
                {"B": "Option B"},
                {"C": "Option C"},
                {"D": "Option D"},
            ]
            
            correct_answer = random.choice(["A", "B", "C", "D"])
            questions.append(
                Question(
                    subject=instance,
                    question=question_text,
                    answers=answers,
                    correct_answer=correct_answer,
                )
            )
        
        
        Question.objects.bulk_create(questions)
