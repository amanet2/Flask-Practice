from flask import Flask

app = Flask(__name__)

from app import views

import lib.clients as clients
import utils.lookup_utils as file_utils
import config

app.weather_interface = clients.ControlClient(config.api_key,config.units)

for city in config.city_map:
    c_c = file_utils.get_city_code(config.local_city_data,city[0],city[1])
    app.weather_interface.add_weather_controller(c_c)
