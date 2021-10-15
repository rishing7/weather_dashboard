from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests
import json


@require_http_methods(["POST"])
def index(request):
    """
        @apiDescription Get City's weather information.
        This endpoint could help to find the city's weather information.

        @api {post} /weather/info/ City's Weather

        @apiName City's Weather
        @apiGroup Weather

        @apiHeader {String} Content-Type application/json

        @apiParam {String} city name of the city

        @apiParamExample {json} Request-Example: User Login
        {
            "city": "Hyderabad"
        }

         @apiSuccessExample {json} Success-Response:
        {
            "city": "Hyderabad",
            "information": {
                "temperature": 82.81,
                "description": "haze"
            },
            "code": 200
        }

        @apiErrorExample {json} Error-Response: For invalid city name

            HTTP/1.1 400 Bad Request
        {
            "city": "Hyderabaad",
            "information": {
                "error": "Invalid city name."
            },
            "code": 400
        }
        @apiError   MethodNotAllowed method not allowed to access 405
    """
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=af93c68dc017847cc2be5c7cd72d2ddc'
    data = json.loads(request.body)
    city = data.get('city')
    r = requests.get(url.format(city)).json()
    resp = {}
    if r.get('cod') == 200:
        resp['code'] = 200
        city_weather = {
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
        }
    else:
        resp['code'] = 400
        city_weather = {"error": "Invalid city name."}
    return JsonResponse({"city": city, 'information': city_weather, **resp})
