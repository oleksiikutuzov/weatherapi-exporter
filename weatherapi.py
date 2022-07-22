from prometheus_client import Gauge

_gauges = {
    "temp_c": Gauge("weatherapi_temperature_c", "Temperature in C", ["location"]),
    "temp_f": Gauge("weatherapi_temperature_f", "Temperature in F", ["location"]),
    "wind_mph": Gauge("weatherapi_wind_mph", "Wind speed in mph", ["location"]),
    "wind_kph": Gauge("weatherapi_wind_kph", "Wind speed in kph", ["location"]),
    "wind_degree": Gauge("weatherapi_wind_degree", "Wind direction in degrees", ["location"]),
    "pressure_mb": Gauge("weatherapi_pressure_mb", "Pressure in mb", ["location"]),
    "pressure_in": Gauge("weatherapi_pressure_in", "Pressure in in", ["location"]),
    "precip_mm": Gauge("weatherapi_precip_mm", "Precipitation in mm", ["location"]),
    "precip_in": Gauge("weatherapi_precip_in", "Precipitation in in", ["location"]),
    "humidity": Gauge("weatherapi_humidity", "Humidity", ["location"]),
    "cloud": Gauge("weatherapi_cloud", "Cloudiness", ["location"]),
    "feelslike_c": Gauge("weatherapi_feelslike_c", "Feels like in C", ["location"]),
    "feelslike_f": Gauge("weatherapi_feelslike_f", "Feels like in F", ["location"]),
    "vis_km": Gauge("weatherapi_vis_km", "Visibility in km", ["location"]),
    "vis_miles": Gauge("weatherapi_vis_miles", "Visibility in miles", ["location"]),
    "uv": Gauge("weatherapi_uv", "UV index", ["location"]),
    "gust_mph": Gauge("weatherapi_gust_mph", "Gust speed in mph", ["location"]),
    "gust_kph": Gauge("weatherapi_gust_kph", "Gust speed in kph", ["location"]),

    "co": Gauge("weatherapi_co", "CO index", ["location"]),
    "no2": Gauge("weatherapi_no2", "NO2 index", ["location"]),
    "o3": Gauge("weatherapi_o3", "O3 index", ["location"]),
    "so2": Gauge("weatherapi_so2", "SO2 index", ["location"]),
    "pm2_5": Gauge("weatherapi_pm2_5", "PM2.5 index", ["location"]),
    "pm10": Gauge("weatherapi_pm10", "PM10 index", ["location"]),
    "us_epa_index": Gauge("weatherapi_us_epa_index", "US EPA index", ["location"]),
    "gb_defra_index": Gauge("weatherapi_gb_defra_index", "GB DEFRA index", ["location"]),

}


def extract_temp(data):

    location = data['location']['name'] + ', ' + \
        data['location']['region'] + ', ' + data['location']['country']

    temp_c = data['current']['temp_c']
    temp_f = data['current']['temp_f']
    wind_mph = data['current']['wind_mph']
    wind_kph = data['current']['wind_kph']
    wind_degree = data['current']['wind_degree']
    pressure_mb = data['current']['pressure_mb']
    pressure_in = data['current']['pressure_in']
    precip_mm = data['current']['precip_mm']
    precip_in = data['current']['precip_in']
    humidity = data['current']['humidity']
    cloud = data['current']['cloud']
    feelslike_c = data['current']['feelslike_c']
    feelslike_f = data['current']['feelslike_f']
    vis_km = data['current']['vis_km']
    vis_miles = data['current']['vis_miles']
    uv = data['current']['uv']
    gust_mph = data['current']['gust_mph']
    gust_kph = data['current']['gust_kph']

    co = data['current']['air_quality']['co']
    no2 = data['current']['air_quality']['no2']
    o3 = data['current']['air_quality']['o3']
    so2 = data['current']['air_quality']['so2']
    pm2_5 = data['current']['air_quality']['pm2_5']
    pm10 = data['current']['air_quality']['pm10']
    us_epa_index = data['current']['air_quality']['us-epa-index']
    gb_defra_index = data['current']['air_quality']['gb-defra-index']

    _gauges['temp_c'].labels(location=str(location)).set(temp_c)
    _gauges['temp_f'].labels(location=str(location)).set(temp_f)
    _gauges['wind_mph'].labels(location=str(location)).set(wind_mph)
    _gauges['wind_kph'].labels(location=str(location)).set(wind_kph)
    _gauges['wind_degree'].labels(location=str(location)).set(wind_degree)
    _gauges['pressure_mb'].labels(location=str(location)).set(pressure_mb)
    _gauges['pressure_in'].labels(location=str(location)).set(pressure_in)
    _gauges['precip_mm'].labels(location=str(location)).set(precip_mm)
    _gauges['precip_in'].labels(location=str(location)).set(precip_in)
    _gauges['humidity'].labels(location=str(location)).set(humidity)
    _gauges['cloud'].labels(location=str(location)).set(cloud)
    _gauges['feelslike_c'].labels(location=str(location)).set(feelslike_c)
    _gauges['feelslike_f'].labels(location=str(location)).set(feelslike_f)
    _gauges['vis_km'].labels(location=str(location)).set(vis_km)
    _gauges['vis_miles'].labels(location=str(location)).set(vis_miles)
    _gauges['uv'].labels(location=str(location)).set(uv)
    _gauges['gust_mph'].labels(location=str(location)).set(gust_mph)
    _gauges['gust_kph'].labels(location=str(location)).set(gust_kph)

    _gauges['co'].labels(location=str(location)).set(co)
    _gauges['no2'].labels(location=str(location)).set(no2)
    _gauges['o3'].labels(location=str(location)).set(o3)
    _gauges['so2'].labels(location=str(location)).set(so2)
    _gauges['pm2_5'].labels(location=str(location)).set(pm2_5)
    _gauges['pm10'].labels(location=str(location)).set(pm10)
    _gauges['us_epa_index'].labels(location=str(location)).set(us_epa_index)
    _gauges['gb_defra_index'].labels(
        location=str(location)).set(gb_defra_index)
