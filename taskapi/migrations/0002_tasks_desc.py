# Generated by Django 3.2 on 2023-04-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='desc',
            field=models.CharField(default='', max_length=700),
        ),
    ]