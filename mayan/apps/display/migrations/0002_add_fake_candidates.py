from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('display', '0001_initial'),
    ]

    def insertData(apps, schema_editor):
        Candidate = apps.get_model("display","Candidate")
        user = Candidate(candidate_name = "Yenlin Kuo", high_school = "Central Bucks West", gpa_score = 4.0, exam_score = 1580)
        user.save()
    operations = [
        migrations.RunPython(insertData),
    ]
