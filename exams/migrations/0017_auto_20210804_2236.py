# Generated by Django 3.2.5 on 2021-08-05 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0016_rename_examsubmission_examattempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examattempt',
            name='guess1',
            field=models.IntegerField(default=0, verbose_name='Problem 1 response'),
        ),
        migrations.AlterField(
            model_name='examattempt',
            name='guess2',
            field=models.IntegerField(default=0, verbose_name='Problem 2 response'),
        ),
        migrations.AlterField(
            model_name='examattempt',
            name='guess3',
            field=models.IntegerField(default=0, verbose_name='Problem 3 response'),
        ),
        migrations.AlterField(
            model_name='examattempt',
            name='guess4',
            field=models.IntegerField(default=0, verbose_name='Problem 4 response'),
        ),
        migrations.AlterField(
            model_name='examattempt',
            name='guess5',
            field=models.IntegerField(default=0, verbose_name='Problem 5 response'),
        ),
    ]