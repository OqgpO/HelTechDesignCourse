from django.conf.urls import url, include
from events.models import Event
from contacts.models import Speaker, Organisation
from rest_framework import routers
from api.views import *


router = routers.DefaultRouter()
router.register(r'speakers', SpeakerViewSet)
router.register(r'events', EventViewSet)
router.register(r'organisations', OrganisationViewSet)
router.register(r'partners', PartnerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^events/past/(?P<limit>[0-9]+)$', pastEvents ),
    url(r'^events/future/(?P<limit>[0-9]+)$', futureEvents ),
    url(r'^events/current$', currentEvent ),
    url(r'^events/(?P<eventId>[0-9]+)/keynote$', keynote ),
    url(r'^events/(?P<eventId>[0-9]+)/panel$', panel ),
    url(r'^events/(?P<eventId>[0-9]+)/demo$', demo ),

]
