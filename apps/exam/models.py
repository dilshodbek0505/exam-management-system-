from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

from apps.common.models import BaseModel

User = get_user_model()


class Subject(BaseModel):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self) -> str:
        return self.name

class Question(BaseModel):
    subject = models.ForeignKey(Subject, models.CASCADE, related_name='questions', verbose_name=_('Subject'))
    question = models.TextField(verbose_name=_('Question'))
    answers = models.JSONField(default=list, verbose_name=_('Answers'))
    correct_answer = models.CharField(max_length=1, verbose_name=_('Correct answer'))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self) -> str:
        return self.subject.name

class Exam(BaseModel):
    subject = models.ForeignKey(Subject, models.CASCADE, related_name='exams', verbose_name=_('Subject'))
    students = models.ManyToManyField(User, related_name='exams', verbose_name=_('Students'))

    title = models.CharField(max_length=128, verbose_name=_('Titile'))
    description = models.TextField(verbose_name=_('Description'))
    question_counts = models.PositiveIntegerField(default=5, verbose_name=_('Question counts'))
    pass_percentage = models.FloatField(default=0.0, verbose_name=_('Pass percentage'))

    start_time = models.DateTimeField(verbose_name=_('Start time'))
    end_time = models.DateTimeField(verbose_name=_('End time'))

    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = _("Exams")
    
    def __str__(self) -> str:
        return self.title

class Test(BaseModel):
    exam = models.ForeignKey(Exam, models.CASCADE, related_name='tests', verbose_name=_('Exam'))
    student = models.ForeignKey(User, models.CASCADE, related_name='tests', verbose_name=_('Student'))

    correct_answers_count = models.PositiveIntegerField(default=0, verbose_name=_('Correct answers count'))
    wrong_answers_count = models.PositiveIntegerField(default=0, verbose_name=_('Wrong answers count'))
    percentage = models.FloatField(default=0.0, verbose_name=_('Percentage'))
    is_pass = models.BooleanField(default=False)

    

    def __str__(self) -> str:
        return self.exam.title

class TestItem(BaseModel):
    test = models.ForeignKey(Test, models.CASCADE, related_name='items', verbose_name=_('Test'))
    question = models.ForeignKey(Question, models.CASCADE, related_name='test_items', verbose_name=_('Question'))
    user_answer = models.CharField(max_length=1, verbose_name=_('User answer'), null=True, blank=True)
    is_true = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Test item")
        verbose_name_plural = _("Test items")

    def __str__(self) -> str:
        return self.test.exam.title

            







    

