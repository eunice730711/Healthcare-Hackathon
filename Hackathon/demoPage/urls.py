from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^demoPage/$', views.post_list),
    url(r'^loginInput/$', views.login_input),
    url(r'^registerInput/$', views.register_input),
    url(r'^searchInput/$', views.search_input, name='searchInput'),
    url(r'^register/$', views.register, name='register'),
    url(r'^patienthistory/$', views.patienthistory, name='patienthistory'),
    url(r'^patientrisk/$', views.patientrisk, name='patientrisk'),
]
