import requests
import datetime
from django.utils import timezone
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def include_external(url):
	include = requests.get(url)
	include_safe = mark_safe(include.text)
	return include_safe

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def get_unitlink(onr):
    # return 'bla{}'.format(onr)
    url = 'https://search-1.q.icts.kuleuven.be/v2/organigram/ou/{}'.format(onr)
    # import pdb; pdb.set_trace()
    r = requests.get(url)
    unit = r.json()
    unitname = unit['_source']['ouDescription']
    return '<a href="{}">{}</a>'.format(onr, unitname)

# @register.simple_tag
# def get_person():
#     url = 'https://webwsp.aps.kuleuven.be/esap/public/odata/sap/zh_person_srv/Persons?$format=json&$filter=userId%20eq%20%27u0010287%27'
#     # params = {'year': year, 'author': author}
#     r = requests.get(url)
#     # r = requests.get(url, params=params)
#     people = r.json()
#     # this returns a list of all people from the search done by the params:
#     # all_people = people['d']['results']
#     # this return only the first item from the list of people:
#     person_new = people['d']['results'][0]
#     # person_new = person['nr']
#     return person_new