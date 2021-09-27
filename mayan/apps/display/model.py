from django.db import models
from django.utils.translation import ugettext_lazy as _

class Candidate(models.Model):
    candidate_name=models.CharField(
        max_length=60, verbose_name=_('Candidate Name')
        )
    reviewer_name=models.CharField(
        max_length=60, verbose_name=_('Reviewer Name')
        )
    test_score=models.FloatField(
        verbose_name=_('Test Socre')
    )
    experience_score=models.FloatField(
        verbose_name=_('Experience Socre')
    )
    skills_score=models.FloatField(
        verbose_name=_('Skills Score')
    )

class Meta:
        verbose_name = _('Candidate')
        verbose_name_plural = _('Candidate')
