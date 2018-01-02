from django.conf.urls import url
from . import views

app_name = 'sensors'

urlpatterns = [

    url(r'^$', views.index,name='index'),

    url(r'^tankReading/$',views.WaterTankView.as_view(),name='tank'),

    url(r'^tapReading/$',views.WaterTapView.as_view(),name='tap'),

    url(r'^addreading/$', views.add_reading),

]