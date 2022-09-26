# Generated by Django 4.0.7 on 2022-09-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0088_auto_20220921_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitinquiry',
            name='status',
            field=models.CharField(choices=[('ACC', 'Accepted'), ('REJ', 'Rejected'), ('NEW', 'Pending'), ('HOLD', 'On hold')], default='NEW', help_text='The current status of the petition.', max_length=5),
        ),
    ]