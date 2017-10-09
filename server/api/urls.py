from django.conf.urls import url, include
from events.models import Event
from contacts.models import Speaker, Organisation
from rest_framework import routers, serializers, viewsets

from . import views

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'title', 'date_organised', 'description', 'speaker')

class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker
        fields = ('url', 'full_name', 'introduction', 'portrait', 'organisation')

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ('url', 'name', 'site_address', 'logo', 'is_partner')

        
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    
class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.filter(is_partner=True)
    serializer_class = OrganisationSerializer

router = routers.DefaultRouter()
router.register(r'speakers', SpeakerViewSet)
router.register(r'events', EventViewSet)
router.register(r'organisations', OrganisationViewSet)
router.register(r'partners', PartnerViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
]
