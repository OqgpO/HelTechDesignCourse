from events.models import Event
from contacts.models import Speaker, Organisation
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    speakers = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='speaker-detail'
    )

    class Meta:
        model = Event
        fields = ('url', 'title', 'start_time', 'end_time', 'eid', 'programme', 'description', 'attending_count', 'cover_uri', 'speakers')

class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    organisation = OrganisationSerializer(many=False, read_only=True)

    class Meta:
        model = Speaker
        fields = ('url', 'full_name', 'introduction', 'portrait', 'organisation', 'event', 'role')

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ('url', 'name', 'site_address', 'logo', 'is_partner')
