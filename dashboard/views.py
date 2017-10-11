from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import coreapi
import json
from django.http import Http404,HttpRequest

# Create your views here.

#View for home page. Request to get the data from the server is sent.
#When the data is recieved, it is stored in the static folder as a json file.
#Home paga requests data of each model from server.
def index(request):
    data = coreapi.Client()
    schema = data.get("http://10.0.3.23:2469/household")
    with open('static/json/household.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/farm")
    with open('static/json/farm.json', 'w') as outfile:
	    json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/well")
    with open('static/json/well.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/member")
    with open('static/json/member.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/season")
    with open('static/json/season.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/crop")
    with open('static/json/crop.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/storage")
    with open('static/json/storage.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/yield")
    with open('static/json/yield.json', 'w') as outfile:
        json.dump(schema, outfile)
    return render(request,'dashboard/index.html')   

#View for charts.
#It requests data of just season and crop models as it doesn't need others.
def showcharts(request):
    data = coreapi.Client()
    schema = data.get("http://10.0.3.23:2469/season")
    with open('static/json/season.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/crop")
    with open('static/json/crop.json', 'w') as outfile:
        json.dump(schema, outfile)
    return render(request,'dashboard/charts.html')

#View for charts.
#It requests data of all models except yield as it doesn't need it.
def showmaps(request):
    data = coreapi.Client()
    schema = data.get("http://10.0.3.23:2469/household")
    with open('static/json/household.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/farm")
    with open('static/json/farm.json', 'w') as outfile:
	    json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/well")
    with open('static/json/well.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/season")
    with open('static/json/season.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/crop")
    with open('static/json/crop.json', 'w') as outfile:
        json.dump(schema, outfile)
    schema = data.get("http://10.0.3.23:2469/storage")
    with open('static/json/storage.json', 'w') as outfile:
        json.dump(schema, outfile)
    return render(request,'dashboard/maps.html')

#View for charts.
#It requests data of just well model as it doesn't need others.
def showwells(request):
    data = coreapi.Client()
    schema = data.get("http://10.0.3.23:2469/well")
    with open('static/json/well.json', 'w') as outfile:
        json.dump(schema, outfile)
    return render(request,'dashboard/wells.html')