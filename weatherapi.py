from prometheus_client import Gauge
import json

_gauges = {
    "temp": Gauge("weatherapi_temperature", "Temperature in C", ["location"]),
}


# def extract_metrics(logger, request_content):

#     data = request_content

#     if data['status'] != 'ok':
#         logger.info(f"Status not ok: {data['status']}")
#     else:
#         _extract_aqi(data)


def extract_temp(data):

    value = data['current']['temp_c']

    location = data['location']['name'] + ', ' + \
        data['location']['region'] + ', ' + data['location']['country']

    _gauges['temp'].labels(location=str(location)).set(value)
