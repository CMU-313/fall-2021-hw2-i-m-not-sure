from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('display', '0002_add_fake_candidates'),
    ]

    def insertData(apps, schema_editor):
        CandidateReview = apps.get_model("display","CandidateReview")
        review = CandidateReview(reviewer_name = "Michael Hilton", candidate_name = "Yenlin Kuo", experience_score = 0, skills_score = 0)
        review.save()
    operations = [
        migrations.RunPython(insertData),
    ]
