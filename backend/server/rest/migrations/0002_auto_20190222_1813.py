# Generated by Django 2.1.7 on 2019-02-22 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_author',
            field=models.TextField(max_length=255),
        ),
    ]
