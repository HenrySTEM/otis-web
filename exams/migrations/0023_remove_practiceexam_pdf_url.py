# Generated by Django 3.2.5 on 2021-08-05 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0022_examattempt_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practiceexam',
            name='pdf_url',
        ),
    ]