 
from rest_framework.serializers import ModelSerializer
from .models import songs
 
 
class ContributersSerializer(ModelSerializer):
    class Meta:
        model = songs
        fields = ('title','iswc')
 