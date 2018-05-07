from django.shortcuts import render
from .models import RegisterData
from .models import HealthData
from .models import RecommendData
from .models import RiskData
from .forms import RegisterForm
from .forms import RiskForm
from django.utils import timezone
import logging
#models
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from sklearn.metrics import mean_squared_error
from mlp_model import DL_model

logger = logging.getLogger(__name__)
"""
def post_list(request):
    patientdata = PatientData.objects.filter(inputTime__isnull=False).order_by('inputTime')
    agelist = list(range(0, 131))
    return render(request, 'blog/patientInput.html', {'patientData': patientdata, 'ageList': agelist})
"""


def post_list(request):
    return render(request, 'blog/patientInput.html', {})


def login(request):
    return render(request, 'blog/login.html', {})


# noinspection PyPep8Naming
def login_input(request):

    logger.error("method >>> " + str(request.method))

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        logger.error("form >>> " + str(form.is_valid()))

        logger.error(form.errors)

    if form.is_valid():
        post = form.save(commit=False)

        userId = post.userId
        logger.error("userId >>> " + userId)

        loginUser = RegisterData.objects.get(userId=userId)
        logger.error("loginUser.userType >>> " + loginUser.userType)

        # doctor
        if loginUser.userType == '1':
            return render(request, 'blog/patientrisk.html', {})

        # patient
        else:

            healthData = HealthData.objects.get(userId=userId)

            registerData = RegisterData.objects.get(userId=userId)
            risk = registerData.riskLevel
            hypertension = loginUser.hypertension
            diabetes = loginUser.diabetes

            if risk == "L":
                riskLevel = "Low"
            elif risk == "M":
                riskLevel = "Medium"
            elif risk == "H":
                riskLevel = "High"
            else:
                riskLevel = "Medium"

            if hypertension == '0' and diabetes == '0':
                recId = risk + '1'
            elif hypertension == '0' and diabetes == '1':
                recId = risk + '2'
            elif hypertension == '1' and diabetes == '0':
                recId = risk + '3'
            elif hypertension == '1' and diabetes == '1':
                recId = risk + '4'
            else:
                recId = "M1"

            logger.error("recId >>> " + recId)

            recommendData = RecommendData.objects.get(recId=recId)
            recommendation_list = recommendData.recommendation_as_list()

            return render(request, 'blog/patientInput.html',
                          {'userId': userId, 'healthData': healthData,
                           'recommendation_list': recommendation_list, 'riskLevel': riskLevel})


def register(request):
    return render(request, 'blog/register.html', {})


def register_input(request):

    logger.error("method >>> " + str(request.method))

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        logger.error("form >>> " + str(form.is_valid()))
        logger.error(form.errors)

    if form.is_valid():
        post = form.save(commit=False)
        age = post.age
        data_list = [age, post.gender, post.height, post.weight,
                     post.diabetes,post.chronicAthens, post.cancer, post.hypertension,0]
        mass = DL_model(data_list)[0][0]
        # This is to create make pretend data for demonstration
        post.riskLevel = 'L' if mass > 63 else ('M' if mass > 58 else 'H')

        post.userType = '0'
        post.inputTime = timezone.now()
        post.save()

    return render(request, 'blog/login.html', {})

# noinspection PyPep8Naming
def search_input(request):

    if request.method == 'POST':
        form = RiskForm(request.POST)

    try:
        if form.is_valid():
            post = form.save(commit=False)
            userId = post.userId
            riskData = RiskData.objects.get(userId=userId)
            return render(request, 'blog/patientrisk.html', {'riskData': riskData})

    except Exception as e:
        logger.error('Patient ID does not exist!')

    return render(request, 'blog/patientrisk.html', {'riskData': {}})

def patienthistory(request):
    return render(request, 'blog/patienthistory.html', {})


def patientrisk(request):
    return render(request, 'blog/patientrisk.html', {})



