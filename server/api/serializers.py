from events.models import Event
from contacts.models import Speaker, Organisation
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('url', 'title', 'start_time', 'end_time', 'eid', 'programme', 'description', 'attending_count', 'cover_uri', 'speaker')

class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speaker
        fields = ('url', 'full_name', 'introduction', 'portrait', 'organisation')

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ('url', 'name', 'site_address', 'logo', 'is_partner')
