from django.urls import path,include
from . import  views
from django.conf.urls import url
from web3auth import views as vw


urlpatterns = [
    path('',views.home),
    url(r'^', include('web3auth.urls')),
    url(r'^login_api/$', vw.login_api, name='web3auth_login_api'),
    url('verification',views.verification,name='verification'),
    url('register',views.register,name='register'),
]
