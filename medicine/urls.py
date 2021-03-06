"""medicine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from symptom.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^splash/', splash),

    url(r'^login_show/', login_show),

    url(r'^auth/', auth),

    url(r'^show_signup/', show_signup),

    url(r'^show_main/', show_main),

    url(r'^register_new/', register_new),

    url(r'^check_symptom/eye/', check_eye),
    url(r'^check_symptom/head/', check_head),
    url(r'^check_symptom/nose/', check_nose),
    url(r'^check_symptom/mouth/', check_mouth),
    url(r'^check_symptom/muscle/', check_muscle),
    url(r'^check_symptom/skin/', check_skin),
    url(r'^check_symptom/digest/', check_digest),
    url(r'^check_symptom/ankle/', check_ankle),
    url(r'^check_symptom/reproduct/', check_reproduct),
    # URL 추가해야 함

    url(r'^answer/', answer),
    url(r'^result/', result),

    #url(r'^show_symptom/', show_symptom),
    
]
