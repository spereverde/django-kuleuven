import requests
from django.shortcuts import render
from django.utils import timezone
from django import template
from .models import Post

from .serializers import PersonSerializer

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
    addresses = person['WorkAddresses']['results'][0]
    # serializer = PersonSerializer(data=person)
	# if serializer.is_valid():
        # person = serializer.save()
        # return render(request, 'blog/person.html', {'person': person})
    return render(request, 'blog/person.html', {'person': person, 'addresses': addresses})
