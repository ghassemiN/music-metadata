from rest_framework.routers import DefaultRouter
from csv_to_json.views import songViewSet
 
 
router = DefaultRouter()
 
router.register('songs', songViewSet)
