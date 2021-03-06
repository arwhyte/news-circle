# Generated by Django 2.1.7 on 2019-03-25 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.TextField(max_length=255)),
                ('group_description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'group',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('invitation_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.TextField(max_length=100)),
                ('status', models.TextField(max_length=100)),
                ('invite_group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.Group')),
            ],
            options={
                'db_table': 'invitation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_title', models.TextField()),
                ('news_description', models.TextField(null=True)),
                ('news_author', models.TextField(max_length=255)),
                ('news_url', models.URLField(null=True)),
                ('news_source', models.TextField(null=True)),
                ('news_content', models.TextField(null=True)),
            ],
            options={
                'db_table': 'news',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.TextField(max_length=100)),
                ('user_key', models.TextField(max_length=100)),
                ('user_email', models.EmailField(error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exist.'}, max_length=254, unique=True)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('friend_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend', to='rest.User')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curUser', to='rest.User')),
            ],
            options={
                'db_table': 'contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('user_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.Group')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.User')),
            ],
            options={
                'db_table': 'user_group',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='invitation',
            name='invitee_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitee', to='rest.User'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='inviter_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to='rest.User'),
        ),
    ]
