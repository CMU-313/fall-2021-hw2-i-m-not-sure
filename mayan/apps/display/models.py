from django.db import models

class Candidate(models.Model):
    candidate_name=models.CharField(max_length=60)
    high_school=models.CharField(max_length=60)
    gpa_score=models.FloatField()
    exam_score=models.FloatField() 

class CandidateReview(models.Model):    
    reviewer_name=models.CharField(max_length=60)
    candidate_name=models.CharField(max_length=60)
    experience_score=models.FloatField()
    skills_score=models.FloatField()