from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import coreapi
import json
from django.http import Http404,HttpRequest

# Create your views here.
def index(request):
    data = coreapi.Client()
    schema = data.get("http://127.0.0.1:8002/household/")
    with open('static/json/household.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/farm/")
    with open('static/json/farm.json', 'w') as outfile:
	    json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/well/")
    with open('static/json/well.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/member/")
    with open('static/json/member.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/season/")
    with open('static/json/season.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/crop/")
    with open('static/json/crop.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/farmphoto/")
    with open('static/json/farmphoto.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/farmvideo/")
    with open('static/json/farmvideo.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/householdphoto/")
    with open('static/json/householdphoto.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/householdaudio/")
    with open('static/json/householdaudio.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/householdvideo/")
    with open('static/json/householdvideo.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/wellphoto/")
    with open('static/json/wellphoto.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/storage/")
    with open('static/json/storage.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://127.0.0.1:8002/storagephoto/")
    with open('static/json/storagephoto.json', 'w') as outfile:
        json.dump(schema, outfile)
    return render(request,'index.html')

def dash(request):
	return render(request,'dashboard.html')