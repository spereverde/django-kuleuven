"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() url: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

from blog.views import get_person, get_unit, get_unit_link, get_unit_name, get_unit_regtree

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'', include('blog.urls')),
    # # person
    # url(r'^wiwo/person/(?P<unr>u[0-9]{7})/$', get_person),
    # # microviews person
    # # unit
    # url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/$', get_unit, name="unit"),
    # # microviews unit
    # url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/link/$', get_unit_link, name="unitlink"),
    # url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/name/$', get_unit_name, name="unitname"),
    # url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/regtree/$', get_unit_regtree, name="regtree"),
    # # url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/children/$', get_unit_children)
    
]
