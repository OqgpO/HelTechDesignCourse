from django.conf.urls import url, include
from events.models import Event
from contacts.models import Speaker, Organisation
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'speakers', SpeakerViewSet)
router.register(r'events', EventViewSet)
router.register(r'organisations', OrganisationViewSet)
router.register(r'partners', PartnerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
