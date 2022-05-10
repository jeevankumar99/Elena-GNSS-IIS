from . import views
from django.urls.conf import path

urlpatterns = [
    path('', views.index, name="index"),
    path('gps_home', views.gps_home, name="gps_home"),
    path('glonass', views.glonass, name="glonass"),
    path('galileo', views.galileo, name="galileo"),
    path('gnss', views.gnss, name="gnss"),
    path('beidou', views.beidou, name="beidou"),
    path('gps', views.gps, name="gps"),
    path('irnss', views.irnss, name="irnss"),
    path('qzss', views.qzss, name="qzss"),
    path('sbas', views.sbas, name="sbas"),
    # path('register', views.register, name="register"),
    # path('logout', views.logout_view, name="logout"),
    # path('login', views.login_view, name="login")
]
