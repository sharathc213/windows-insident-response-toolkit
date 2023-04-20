from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.template.loader import get_template
from django.template import Context, Template
import json
from wir_toolkit.connection import connectionss
import winrm

message=""

def Signin(request):
    return render(request,'Signin.html')

def Dashboard(request,param=None):
    context = {}
    with open('config.json', "r+") as file:
        context["host"] = json.load(file)
        # if message!="":
        if param is not None:
        # Do something with the parameter value
            context["message"]=param
        return render(request,'Dashboard.html',context)

def AddComputer(request):
    return render(request,'AddComputer.html')


def Delete(request,param=None):
    
    if param is not None:
        # Do something with the parameter value
        host=param
        with open('config.json', "r") as file:
            data = json.load(file)
            for idx, obj in enumerate(data):
                if obj['HOST'] == host:
                    data.pop(idx)
                # file.seek(0)
                # json.dump(data, file)
            with open("config.json", 'w') as data_file:
                json.dump(data, data_file)
        
        return redirect("Dashboard")

def Scan(request,param=None):
    context = {}
    if param is not None:
        # Do something with the parameter value
        context["host"]=param
    return render(request,'Scan.html',context)

def addcom(request):
    comname = request.POST['computer']
    password = request.POST['password']
    username = request.POST['username']
    host = request.POST['host']
    entry ={'HOST': host,'NAME':comname,'USER':username,'PASS':password}
    with open('config.json', "r+") as file:
        data = json.load(file)
        flag=False
        for i in data:
            if i['HOST']==host:
                flag=True
 
        if flag==False: 
            data.append(entry)
            file.seek(0)
            json.dump(data, file)
            message = "Computer Added sucessfully"


    return redirect("Dashboard")


def action(request):
    host = request.POST['host']
    action = request.POST['action']

    winrm_session = connectionss(host)

    if action == "1":
        try:
            print("IP Configuration:")
            result = winrm_session.run_cmd('ipconfig', ['/all'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
            
        except:
            print(123)
            return JsonResponse({'msg':'error'})
    
    elif action == "2":
            try:
                print("Groups:")
                result = winrm_session.run_cmd('net', ['localgroup'])
                for result_line in result.std_out.decode('ascii').split("\r\n"):
                    print(result_line)
                    return JsonResponse({'msg':'sucess','action':"IP Configuration"})
            except:
                return JsonResponse({'msg':'error'})
    
    elif action == "3":
        try:
            print("Tasks:")
            result = winrm_session.run_cmd('tasklist', ['/svc'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
         
            return JsonResponse({'msg':'error'})
    elif action == "4":
        try:
            print("Services:")
            result = winrm_session.run_cmd('net', ['start'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
        
            return JsonResponse({'msg':'error'})
    
    elif action == "5":
        try:
            print("Task Scheduler:")
            result = winrm_session.run_cmd('schtasks')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
            
            return JsonResponse({'msg':'error'})
        
    elif action == "6":
        try:
            print("Registry Control:")
            result = winrm_session.run_cmd('reg',['query','HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
            return JsonResponse({'msg':'error'})
    
    elif action == "7":
        try:
            print("Active TCP & UDP ports:")
            result = winrm_session.run_cmd('netstat', ['-ano'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
            return JsonResponse({'msg':'error'})
    elif action == "8":
        try:
            print("File sharing:")
            result = winrm_session.run_cmd('net', ['view'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
            return JsonResponse({'msg':'error'}) 
        
    elif action == "9":
        try:
            print("Files:")
            result = winrm_session.run_cmd('forfiles /D -10 /S /M *.exe /C "cmd /c echo @ext @fname @fdate"')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
            return JsonResponse({'msg':'error'})
        
    elif action == "10":
        try:
            print("Firewall Config:")
            result = winrm_session.run_cmd('netsh firewall show config')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
            return JsonResponse({'msg':'error'})
        
    elif action == "11":
        try:
            print("Sessions with other Systems:")
            result = winrm_session.run_cmd('net use')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
            return JsonResponse({'msg':'error'})
        
    elif action == "12":
        try:
            print("Open Sessions:")
            result = winrm_session.run_cmd('net session')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
            return JsonResponse({'msg':'error'})
    elif action == "13":
        try:
            print("Log Entries:")
            result = winrm_session.run_cmd('wevtutil qe security')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
                return JsonResponse({'msg':'sucess','action':"IP Configuration"})
        except:
            return JsonResponse({'msg':'error'})
    else:
        return JsonResponse({'msg':'error'})















