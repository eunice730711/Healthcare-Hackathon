from django import forms
from .models import RegisterData, RiskData


class RegisterForm(forms.ModelForm):

    class Meta:
        model = RegisterData
        fields = ['userId', 'password', 'age', 'gender', 'height', 'weight', 'race', 'diabetes',
                  'hypertension', 'cancer', 'chronicAthens', 'heartDisease', 'riskLevel', 'userType', 'inputTime']


class RiskForm(forms.ModelForm):

    class Meta:
        model = RiskData
        fields = ['userId', 'wbc', 'rbc', 'hgb', 'hct', 'mcv', 'sarcopeniaRisk', 'inputTime']