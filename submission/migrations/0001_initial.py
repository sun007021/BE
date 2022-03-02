# Generated by Django 3.1 on 2022-03-03 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.common


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
        ('competition', '0001_initial'),
        ('classes', '0001_initial'),
        ('contest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField()),
                ('score', models.FloatField(null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.TextField(null=True)),
                ('on_leaderboard', models.BooleanField(default=False)),
                ('status', models.IntegerField(default=0)),
                ('problem_id', models.ForeignKey(db_column='problem_id', on_delete=django.db.models.deletion.CASCADE, to='problem.problem')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'path',
            },
        ),
        migrations.CreateModel(
            name='SubmissionCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(blank=True, null=True, upload_to=utils.common.upload_to_submission)),
                ('ipynb', models.FileField(blank=True, null=True, upload_to=utils.common.upload_to_submission)),
                ('competition_id', models.ForeignKey(db_column='competition_id', on_delete=django.db.models.deletion.CASCADE, to='competition.competition')),
                ('path', models.ForeignKey(db_column='path', on_delete=django.db.models.deletion.CASCADE, to='submission.path')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'submission_competition',
            },
        ),
        migrations.CreateModel(
            name='SubmissionClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(blank=True, null=True, upload_to=utils.common.upload_to_submission)),
                ('ipynb', models.FileField(blank=True, null=True, upload_to=utils.common.upload_to_submission)),
                ('c_p_id', models.ForeignKey(db_column='c_p_id', on_delete=django.db.models.deletion.CASCADE, to='contest.contest_problem')),
                ('class_id', models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.CASCADE, to='classes.class')),
                ('contest_id', models.ForeignKey(db_column='contest_id', on_delete=django.db.models.deletion.CASCADE, to='contest.contest')),
                ('path', models.ForeignKey(db_column='path', on_delete=django.db.models.deletion.CASCADE, to='submission.path')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'submission_class',
            },
        ),
    ]
