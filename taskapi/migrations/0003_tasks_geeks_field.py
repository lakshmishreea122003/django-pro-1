# Generated by Django 3.2 on 2023-04-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapi', '0002_tasks_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='geeks_field',
            field=models.DateTimeField(null=True),
        ),
    ]