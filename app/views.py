from flask import render_template, request, jsonify
from app import app
import utils.display_utils as stdout
import lib.clients as clients
import utils.net_utils as net_utils
import config

def get_weather(wc: clients.DelegateClient):
    toreach = net_utils.build_request(app.weather_interface.api_base,wc.arg_map,app.weather_interface.api_key)
    j_data = net_utils.send_request(toreach).json()
    print(j_data)
    return j_data

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Buddy'}  # fake user
    posts = [  # fake array of posts

    ]
    for city in app.weather_interface.weather_controllers:
        posts.append(stdout.show_weather_report(get_weather(city),config.desired_reportings))
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)