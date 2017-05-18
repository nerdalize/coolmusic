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

    last_event = venue.events.latest('timestamp')
    print(last_event)

    if data['event']['artist'] == last_event.data['artist'] and data['event']['song_name'] == last_event.data['song_name']:
        print('Not saving, same song')
        return JsonResponse({
            'same': True
        })

    venue.events.create(data=data['event'])

    return JsonResponse({
        'ok': True
    })


@require_http_methods(["POST"])
def status(request):
    ''' POST api.rock-on.space/status {
      "venue": "tnw-hackbattle",
      "loudness": 2,
      "atmosphere": "SKLJDSFLKSJDFSDf",
      "emoji": ":D"
    }'''
    data = json.loads(request.body.decode('utf-8'))
    venue = Venue.objects.get(device_id=data['venue'])

    venue.atmosphere = data['atmosphere']
    venue.loudness = data['loudness']
    venue.emoji = data['emoji']
    venue.save()

    return JsonResponse({
        'ok': True
    })
