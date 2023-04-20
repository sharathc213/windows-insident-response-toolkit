import winrm
import json

def connectionss(host):
    f = open('config.json')
    data = json.load(f)
    for data in data:
        if data['HOST']==host:
            user=data['USER']
            password=data['PASS']
   
    winrm_session = winrm.Session(host, auth=(user, password))
    return winrm_session
