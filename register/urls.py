from django.urls import path,include
from . import  views
from django.conf.urls import url
from web3auth import views as vw
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'registration', views.RegistrationViewSet)


urlpatterns = [
    path('', views.home),
    path('api/', include(router.urls)),
    url(r'^', include('web3auth.urls')),
    url(r'^login_api/$', vw.login_api, name='web3auth_login_api'),
    url('verification',views.verification,name='verification'),
    url('register',views.register,name='register'),

]
