from django.conf.urls import url, include
from . import views

# from django.contrib import admin

from .views import get_person, get_unit, get_unit_link, get_unit_name, get_unit_regtree, get_unit_globtree

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # url(r'^admin/', admin.site.urls),
    
    # person
    url(r'^wiwo/person/(?P<unr>u[0-9]{7})/$', get_person),
    # microviews person
    # unit
    url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/$', get_unit, name="unit"),
    # microviews unit
    url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/link/$', get_unit_link, name="unitlink"),
    url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/name/$', get_unit_name, name="unitname"),
    url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/regtree/$', get_unit_regtree, name="regtree"),
    url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/globtree/$', get_unit_globtree, name="globtree"),
    # url(r'^wiwo/unit/(?P<onr>5[0-9]{7})/children/$', get_unit_children)
]