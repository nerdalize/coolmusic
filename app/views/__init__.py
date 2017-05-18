from .user import *
from .venue import *

from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from app.models import Venue


@require_http_methods(["POST"])
def listening(request):
    data = json.loads(request.body.decode('utf-8'))
    venue = Venue.objects.get(device_id=data['venue'])
    venue.event_set.create(data=data['event'])

    return JsonResponse({
        'ok': True
    })
