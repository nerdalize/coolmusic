
from app.models import Venue, Event
from rest_framework import serializers, viewsets


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('timestamp', 'data')


# Serializers define the API representation.
class VenueSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()

    def get_events(self, obj):
        events = Event.objects.filter(venue=obj).order_by('-timestamp')[:5]
        return EventSerializer(events, many=True).data

    class Meta:
        model = Venue
        fields = ('name', 'lat', 'lng', 'events', 'description')


# ViewSets define the view behavior.
class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
