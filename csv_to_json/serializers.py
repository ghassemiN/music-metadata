 
from rest_framework.serializers import ModelSerializer
from .models import csvfile
 
 
class ContributersSerializer(ModelSerializer):
    class Meta:
        model = csvfile
        fields = ('title','iswc','contributer')
 