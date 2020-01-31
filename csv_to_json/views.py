from django.shortcuts import render
from django.http import HttpResponse
from os.path import dirname
from .models import myfile
import csv
import json
import sys
import os
from collections import defaultdict

# Create your views here.
def index(request):
	context={
	'title': "This is test",
    'desc': "Upload the CSV file",
	}
	return render(request, 'csv_to_json/index.html',context=context)

def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))

        # CSV to JSON
        csvfile = open('upload/' + request.FILES['file'].name, 'rt')
        jsonfile = open('./file.json', 'w')
        fieldnames = ("title","contributors","iswc")
        reader = csv.DictReader( csvfile, fieldnames)
        for row in reader:
        	json.dump(row, jsonfile)
        	jsonfile.write('\n')
        	#Write in to DB
       		intoDB=myfile.objects.create(**row)
       	return HttpResponse("Successful")

    return HttpResponse("Failed")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return ('upload/'+filename)
    
