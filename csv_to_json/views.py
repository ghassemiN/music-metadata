from django.shortcuts import render
from django.http import HttpResponse
from os.path import dirname
from .models import contributers, songs, song_contributer
import csv
import json
import sys
import os
from rest_framework.viewsets import ModelViewSet
from .serializers import ContributersSerializer


class songViewSet(ModelViewSet):
    serializer_class = ContributersSerializer
    queryset = songs.objects.all()
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

        # CSV to Array
        with open('upload/' + request.FILES['file'].name, newline='') as f:
        	render=csv.reader(f)
        	yourlist=list(render)

        #remove first row beacuse it is emty
       	yourlist.remove(yourlist[0])

        #Sort the list to forward empty iswc to bottom of the list
        yourlist = sorted(yourlist, key=lambda x: x[2], reverse=True)

        for i in yourlist:
        	list_contributers=i[1].split('|')

        	song_title=i[0]
        	iswc=i[2]
        	into_song_table=songs.objects.get_or_create(title=song_title,iswc=iswc)
        	into_song_table=songs.objects.last()
        	
        	for index_contributer in list_contributers:
        		into_contrib_table=contributers.objects.get_or_create(contributer=index_contributer)
        		into_contrib_table=contributers.objects.get(contributer=index_contributer)
        		into_song_contributer_table=song_contributer.objects.get_or_create(contributer_id=into_contrib_table.id,song_id=into_song_table.id)

       	return HttpResponse("Successful")

    return HttpResponse("Failed")


def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return ('upload/'+filename)
    
