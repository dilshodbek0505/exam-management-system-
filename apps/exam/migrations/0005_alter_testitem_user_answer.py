# Generated by Django 5.1.2 on 2024-11-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_rename_quetsion_counts_exam_question_counts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testitem',
            name='user_answer',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='User answer'),
        ),
    ]