import lib.clients as clients
import utils.lookup_utils as file_utils
import utils.net_utils as net_utils
import utils.display_utils as stdout
import config

if __name__ == '__main__':
    interface = clients.ControlClient(config.api_key,config.units)


    def get_weather(wc: clients.DelegateClient):
        toreach = net_utils.build_request(interface.api_base,wc.arg_map,interface.api_key)
        j_data = net_utils.send_request(toreach).json()
        print(j_data)
        return j_data

    for city in config.city_map:
        c_c = file_utils.get_city_code(config.city_data,city[0],city[1])
        interface.add_weather_controller(c_c)

    for city in interface.weather_controllers:
        obj = stdout.show_weather_report(get_weather(city),config.desired_reportings)
