
from app.models import Venue, Event
from rest_framework import serializers, viewsets


class EventSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return obj.data

    class Meta:
        model = Event


# Serializers define the API representation.
class VenueSerializer(serializers.ModelSerializer):
    event_set = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Venue
        fields = ('name', 'lat', 'lng', 'event_set')


# ViewSets define the view behavior.
class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
