from django.test import TestCase
import json


class TestWeatherInfo(TestCase):

    def call_endpoint(self, request_data, http_method="post"):
        self.endpoint = "/weather/info/"
        res = getattr(self.client, http_method)(self.endpoint, json.dumps(request_data), "application/json")
        return res.json()

    def test_with_valid_city_name(self):
        resp = self.call_endpoint(request_data={"city": "Mumbai"})
        self.assertEqual(resp["code"], 200)

    def test_with_invalid_city_name(self):
        resp = self.call_endpoint(request_data={"city": "Mumabai"})
        self.assertEqual(resp["code"], 400)