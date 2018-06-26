import requests
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.utils import timezone
from django.utils.safestring import mark_safe
from django import template
from .models import Post


from .serializers import PersonSerializer, UnitSerializer

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# return render(request, 'blog/post_list.html', {'posts': posts})
	return render(request, 'blog/post_kul.html', {'posts': posts})

def get_person(request, unr):
    url = 'https://webwsp.aps.kuleuven.be/esap/public/odata/sap/zh_person_srv/Persons?$format=json&$expand=WorkAddresses&$filter=userId%20eq%20%27{}%27'.format(unr)
    # params = {'year': year, 'author': author}
    r = requests.get(url)
    # r = requests.get(url, params=params)
    people = r.json()
    person = people['d']['results'][0]
    addresses = person['WorkAddresses']['results']
    # serializer = PersonSerializer(data=person)
	# if serializer.is_valid():
        # person = serializer.save()
        # return render(request, 'blog/person.html', {'person': person})
    return render(request, 'blog/person.html', {'person': person, 'addresses': addresses})

# @cache_page(60 * 15)
def get_unit_json(request, onr):
    url = 'https://search-1.q.icts.kuleuven.be/v2/organigram/ou/{}'.format(onr)
    r = requests.get(url)
    unit = r.json()
    return unit['_source']

def get_unit(request, onr):
    is_cached = False
    onr_cached = ('unitnr' in request.session) 
    if onr_cached:
        is_cached = (request.session['unitnr'] == onr)

    if not is_cached:
        url = 'https://search-1.q.icts.kuleuven.be/v2/organigram/ou/{}'.format(onr)
        r = requests.get(url)
        unit = r.json()
        unitdata = unit['_source']
        request.session['unitdata'] = unitdata
        request.session['unitnr'] = unitdata['id']
    
    unitdata = request.session['unitdata']

    return render(request, 'blog/unit.html', {
        'unit': unitdata,
        # 'is_cached': is_cached
        })

def get_unit_link(request, onr):
    unit = get_unit_json(requests, onr)
    unitname = unit['ouDescription']
    unitlink = '<a href="/{}">{}</a>'.format(onr, unitname)
    return render(request, 'blog/unit_link.html', {'unitlink': mark_safe(unitlink)})

def get_unit_name(request, onr):
    unit = get_unit_json(requests, onr)
    unitname = unit['ouDescription']
    return render(request, 'blog/unit_name.html', {'unitname': unitname})

def get_unit_regtree(request, onr):
    unit = get_unit_json(requests, onr)
    return render(request, 'blog/unit_regtree.html', {'unit': unit})

def get_unit_globtree(request, onr):
    unit = get_unit_json(requests, onr)
    return render(request, 'blog/unit_globtree.html', {'unit': unit})