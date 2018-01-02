from django.conf.urls import url

from . import views

app_name = 'LoginPortal'

urlpatterns = [

	url(r'^$',views.indexView,name='home'),
	
	url(r'^register/$',views.UserRegisterView,name='register'),

	url(r'^login/$',views.UserLoginView,name='login'),
]