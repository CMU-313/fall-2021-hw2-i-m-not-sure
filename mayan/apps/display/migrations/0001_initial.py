from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('documents', '0050_auto_20190725_0451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True, primary_key=True, serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'candidate_name', models.CharField(
                        max_length=60, verbose_name='Candidate Name'
                    )
                ),
                (
                    'high_school', models.CharField(
                        max_length=60, verbose_name='High School'
                    )
                ),
                (
                    'gpa_score', models.FloatField(
                        verbose_name='GPA Score'
                    )
                ),
                (
                    'exam_score', models.FloatField(
                        verbose_name='Exam Score'
                    )
                ),
            ],
            options={
                'ordering': ('candidate_name',),
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='CandidateReview',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True, primary_key=True, serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'reviewer_name', models.CharField(
                        max_length=60, verbose_name='Reviewer Name'
                    )
                ),
                (
                    'candidate_name', models.CharField(
                        max_length=60, verbose_name='Candidate Name'
                    )
                ),                
                (
                    'experience_score', models.FloatField(
                        verbose_name='Experiences Score'
                    )
                ),
                (
                    'skills_score', models.FloatField(
                        verbose_name='Skills Score'
                    )
                ),
            ],
            options={
                'ordering': ('reviewer_name',),
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
