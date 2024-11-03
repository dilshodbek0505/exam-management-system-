from django.contrib import admin

from .models import Subject, Question, Exam, Test, TestItem


admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Test)
admin.site.register(TestItem)
