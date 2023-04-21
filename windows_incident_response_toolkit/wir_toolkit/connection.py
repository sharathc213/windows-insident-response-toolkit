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
    # try:
    #         print("IP Configuration:")
    #         result = winrm_session.run_cmd('ipconfig', ['/all'])
    #         for result_line in result.std_out.decode('ascii').split("\r\n"):
    #             print(result_line)
    # except:
    #     return winrm_session
                
    return winrm_session
