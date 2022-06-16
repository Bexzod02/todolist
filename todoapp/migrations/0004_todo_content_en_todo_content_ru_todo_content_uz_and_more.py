# Generated by Django 4.0.4 on 2022-05-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='content_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='title_en',
            field=models.CharField(max_length=221, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='title_ru',
            field=models.CharField(max_length=221, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='title_uz',
            field=models.CharField(max_length=221, null=True),
        ),
    ]
