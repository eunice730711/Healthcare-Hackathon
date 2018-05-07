from django.contrib import admin
from .models import RegisterData
from .models import HealthData
from .models import RecommendData
from .models import RiskData

admin.site.register(RegisterData)
admin.site.register(HealthData)
admin.site.register(RecommendData)
admin.site.register(RiskData)