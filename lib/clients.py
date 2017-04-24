class DelegateClient:
    def __init__(self,c_id):
        self.city_id = c_id
        self.arg_map = {}

class ControlClient:
    def __init__(self,creds,unts):
        self.api_key = creds
        self.api_base = f'http://api.openweathermap.org/data/2.5/weather?'
        self.units = unts
        self.weather_controllers = []

    def add_weather_controller(self,c_id):
        wc = DelegateClient(c_id)
        wc.arg_map = { 'id':f'{c_id}',
                     'units': f'{self.units}',
                     'appid': f'{self.api_key}'}
        self.weather_controllers.append(wc)

