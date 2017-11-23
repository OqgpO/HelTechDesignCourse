from events.models import Event, Place
from contacts.models import Speaker, Organisation
from rest_framework import serializers

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('url', 'id', 'name', 'streetaddr')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    speakers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='speaker-detail'
    )
    place = PlaceSerializer(many=False, read_only=True)

    class Meta:
        model = Event
        fields = ('url', 'id', 'title', 'start_time', 'end_time', 'eid', 'programme', 'description', 'attending_count', 'cover_uri', 'place', 'speakers')

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ('url', 'id', 'name', 'site_address', 'logo', 'is_partner')

class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    organisation = OrganisationSerializer(many=False, read_only=True)

    class Meta:
        model = Speaker
        fields = ('url', 'id', 'full_name', 'title', 'introduction', 'portrait', 'organisation', 'event', 'role')

