import json
import codecs
import traceback
import requests

def unarch_json(path: str) -> dict:
    with codecs.open(path, "r",encoding='utf-8') as f:
        d = json.loads(f.read())
        return d

def get_city_code(srcfile: str, city: str, state: str) -> int:
    j_data = unarch_json(srcfile)
    for key in j_data:
        try:
            if(key['name'] == city and key['country'] == state):
                return key['id']
        except UnicodeEncodeError:
            print(traceback.format_exc())
    return -1

def net_get_city_code(srcurl: str, city: str, state: str) -> int:
    j_data = requests.get(srcurl).json()
    try:
        print(j_data)
    except UnicodeEncodeError:
        print(traceback.format_exc())
    return -1