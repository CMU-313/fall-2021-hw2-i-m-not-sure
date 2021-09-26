from django.db import models

class Candidate(models.Model):
    candidate_name=models.CharField(max_length=60)
    reviewer_name=models.CharField(max_length=60)
    test_score=models.FloatField()
    experience_score=models.FloatField()
    skills_score=models.FloatField()
