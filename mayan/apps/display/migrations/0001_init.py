from django.db import migrations, models
from django.db.models.fields import AutoField, CharField, FloatField
from django.db import models
from django.core.management import call_command

fixture = 'initial_data'

class Migration(migrations.Migration):
    dependencies = [   
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                (
                    'id', models.AutoField(
                        verbose_name='ID', serialize=False, auto_created=True,
                        primary_key=True
                    )
                ),
                (
                    'candidate_name', models.CharField(
                        max_length=60, verbose_name='Candidate Name'
                    )
                ),
                (
                    'reviewer_name', models.CharField(
                        max_length=60, verbose_name='Reviewer Name'
                    )
                ),
                ('test_score', models.FloatField(verbose_name='Test Socre')),
                ('experience_score', models.FloatField(verbose_name='Experience Socre')),
                ('skills_score', models.FloatField(verbose_name='Skills Score')),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidate',
            },
        ),
    ]
    def load_fixture(self, schema_editor):
        call_command('loaddata', fixture, app_label='display')