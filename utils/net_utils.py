import requests

def build_request(base_url: str,arglist: dict, creds: str) -> str:
    ep_str = base_url
    for arg in arglist:
        if 'id' != arg:
            ep_str += '&'
        arg_str = f'{arg}={arglist[arg]}'
        ep_str += arg_str
    # print(ep_str)
    return ep_str

def send_request(endp):
    resp = requests.get(endp)
    return resp
