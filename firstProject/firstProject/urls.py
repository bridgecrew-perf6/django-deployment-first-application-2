"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path	#old
from django.conf.urls import url;	#new

from firstApp import views;
from multiViewsApp import views as v1;

#from App1 import views;
#from App2 import views;
#approach1
from App1.views import f11;
from App2.views import f22;
#approach2
from App1 import views as v11;
from App2 import views as v22;

#multiple-urls for same-view
from firstApp import views;



urlpatterns = [
    path('admin/', admin.site.urls),
	
	#firstApp
	#url(r'^welcome/',views.display) #old-method
	path('welcome/',views.display),
	
	#multiViewsApp
	path('mrng/',v1.f1),
	path('aftr/',v1.f2),
	path('even/',v1.f3),
	
	#approach1
	path('hello/',f11),
	path('datetime/',f22),
	
	#approach2
	path('hello1/',v11.f11),
	path('datetime1/',v22.f22),
	
	#multiple-views for same-view
	url('$', views.display), 
	url('test/', views.display) 
	
];
