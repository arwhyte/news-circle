# Generated by Django 2.1.7 on 2019-03-25 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_auto_20190325_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='invite_group_id',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='invitee_id',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='inviter_id',
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
    ]
