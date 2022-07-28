from prometheus_client import start_http_server
import logging
import time
import sys
import os
import weatherapi
import signal
from threading import Event
import requests

"""
Environment variable labels used to read values from.
HOST_PORT               Sets port to run the prometheus http server, default to 9090
LOCATION                Sets the location to use for the data export
WEATHERAPI_TOKEN        Sets weatherapi token
UPDATE_INTERVAL         Sets interval between updates in seconds, default is 10.0 seconds
"""

PORT_LABEL = 'HOST_PORT'
LOCATION_LABEL = 'LOCATION'
TOKEN_LABEL = 'WEATHERAPI_TOKEN'
TIMEOUT_LABEL = 'UPDATE_INTERVAL'

exit = Event()


def signalShuttdown(self, *args):
    exit.set()


config = {
    'host_port': 9090,
    'location': '',
    'token': '',
    'timeout': 10.0
}


if PORT_LABEL in os.environ:
    config['host_port'] = int(os.environ[PORT_LABEL])

if LOCATION_LABEL in os.environ:
    config['location'] = os.environ[LOCATION_LABEL]

if TOKEN_LABEL in os.environ:
    config['token'] = os.environ[TOKEN_LABEL].strip()

if TIMEOUT_LABEL in os.environ:
    config['timeout'] = float(os.environ[TIMEOUT_LABEL])


def create_logger(scope):
    logger = logging.getLogger(scope)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%dT%H:%M:%S"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


if __name__ == '__main__':
    logger = create_logger('weatherapi-exporter')

    if not config['token']:
        logger.error(
            f"No token provided. Please provide token.")
        sys.exit(1)

    if not config['location']:
        logger.error(
            f"Location not set. Please set it in the environment variables.")
        sys.exit(1)

    start_http_server(config['host_port'])

    signal.signal(signal.SIGTERM, signalShuttdown)
    signal.signal(signal.SIGHUP, signalShuttdown)
    signal.signal(signal.SIGINT, signalShuttdown)
    signal.signal(signal.SIGABRT, signalShuttdown)

    while not exit.is_set():

        r = requests.get('http://api.weatherapi.com/v1/current.json?key=' +
                         config['token'] + '&q=' + config['location'] + '&aqi=yes')

        if r.status_code == 200:
            weatherapi.extract_temp(r.json())
            logger.info(f"Request succeeded")
        else:
            logger.error(
                f"Request did not result in a successful status, {r.json()['error']['message']}")

        sleepTime = 0.0

        while (config['timeout'] > sleepTime) and not exit.is_set():
            time.sleep(0.1)
            sleepTime += 0.1

    logger.info("shutting down")
