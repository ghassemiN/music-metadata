from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import csvfile
import csv
import sys
import os
from rest_framework.viewsets import ModelViewSet
from .serializers import ContributersSerializer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict 


class songViewSet(ModelViewSet):
    serializer_class = ContributersSerializer
    queryset = csvfile.objects.all()

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
    	df = pd.read_csv('upload/' + request.FILES['file'].name)
    	df = df.groupby('iswc').agg({'title':'first', 'contributors': '|' .join}).reset_index()
    	df['contributors'] = (df['contributors'].str.split('|').apply(lambda x: OrderedDict.fromkeys(x).keys()).str.join('|'))
    	df.to_csv('upload/ress.csv')

    with open('upload/ress.csv', newline='') as f:
    	reader=csv.reader(f)
    	for i in reader:
    		create=csvfile.objects.get_or_create(title=i[2],iswc=i[1],contributer=i[3])
    		
    	#If it is successful then redirect to api
    	return redirect('../api')

    return HttpResponse("Failed")


def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return ('upload/'+filename)