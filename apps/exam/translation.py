from modeltranslation.translator import TranslationOptions, register

from .models import Exam, Subject, Question, Test, TestItem



@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'answers')
