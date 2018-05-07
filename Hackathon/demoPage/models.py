from django.db import models
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class RegisterData(models.Model):

    userId = models.CharField(max_length=10)
    password = models.CharField(max_length=10, blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    race = models.CharField(max_length=10, blank=True, null=True)

    diabetes = models.CharField(max_length=10, blank=True, null=True)
    hypertension = models.CharField(max_length=10, blank=True, null=True)
    cancer = models.CharField(max_length=10, blank=True, null=True)
    chronicAthens = models.CharField(max_length=10, blank=True, null=True)
    heartDisease = models.CharField(max_length=10, blank=True, null=True)

    riskLevel = models.CharField(max_length=1, blank=True, null=True)

    userType = models.CharField(max_length=1, blank=True, null=True)
    inputTime = models.DateTimeField(default=timezone.now(), blank=True, null=True)

    def __unicode__(self):
        return self.userId


class HealthData(models.Model):

    userId = models.CharField(max_length=10, blank=True, null=True)

    cardioMin = models.CharField(max_length=10, blank=True, null=True)
    sportsMin = models.CharField(max_length=3, blank=True, null=True)
    strengthMin = models.CharField(max_length=10, blank=True, null=True)
    weightMin = models.CharField(max_length=10, blank=True, null=True)

    breakfastkCal = models.CharField(max_length=10, blank=True, null=True)
    lunchkCal = models.CharField(max_length=10, blank=True, null=True)
    dinnerkCal = models.CharField(max_length=10, blank=True, null=True)

    breakfastProtein = models.CharField(max_length=10, blank=True, null=True)
    lunchProtein = models.CharField(max_length=10, blank=True, null=True)
    dinnerProtein = models.CharField(max_length=10, blank=True, null=True)

    breakfastCarb = models.CharField(max_length=10, blank=True, null=True)
    lunchCarb = models.CharField(max_length=10, blank=True, null=True)
    dinnerCarb = models.CharField(max_length=10, blank=True, null=True)

    breakfastFat = models.CharField(max_length=10, blank=True, null=True)
    lunchFat = models.CharField(max_length=10, blank=True, null=True)
    dinnerFat = models.CharField(max_length=10, blank=True, null=True)

    inputTime = models.DateTimeField(default=timezone.now(), blank=True, null=True)

    def __unicode__(self):
        return self.userId


class RiskData(models.Model):

    userId = models.CharField(max_length=10, blank=True, null=True)

    wbc = models.CharField(max_length=10, blank=True, null=True)
    rbc = models.CharField(max_length=10, blank=True, null=True)
    hgb = models.CharField(max_length=10, blank=True, null=True)
    hct = models.CharField(max_length=10, blank=True, null=True)
    mcv = models.CharField(max_length=10, blank=True, null=True)

    sarcopeniaRisk = models.CharField(max_length=10, blank=True, null=True)

    inputTime = models.DateTimeField(default=timezone.now(), blank=True, null=True)

    def __unicode__(self):
        return self.userId


class RecommendData(models.Model):

    recId = models.CharField(max_length=10)
    recommendation = models.TextField(max_length=5000)

    def recommendation_as_list(self):
        return self.recommendation.split('.')

    def __unicode__(self):
        return self.recId

