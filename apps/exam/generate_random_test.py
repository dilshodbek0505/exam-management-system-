import random

from apps.exam.models import Question, Subject


def generate():
    subjects = Subject.objects.all()
        
    for subject in subjects:
        for _ in range(10):
            questions = []
            for i in range(100):
                question_text = f"Test question {i+1} for {subject.name}"
                    
                answers = [
                    {"option": "A", "text": f"Answer A for {question_text}"},
                    {"option": "B", "text": f"Answer B for {question_text}"},
                    {"option": "C", "text": f"Answer C for {question_text}"},
                    {"option": "D", "text": f"Answer D for {question_text}"}
                ]
                    
                    
                correct_answer = random.choice(["A", "B", "C", "D"])

                    
                questions.append(
                    Question(
                        subject=subject,
                        question=question_text,
                        answers=answers,
                        correct_answer=correct_answer
                    )
                )

                
            Question.objects.bulk_create(questions)

