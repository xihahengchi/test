#encoding=utf-8
import requests,json,sys
#address=r'http://172.20.10.4:8080/front/register'
address = "http://"+sys.argv[1]+'/front/register'
'''用户注册'''
def register():
    global pwd
    print("*"*40)
    print("register--------")
    data=json.dumps({'username':'ksh','password':'ksh','password2':'ksh'})
    r=requests.post(address,data=data)
    print(r.url)
    print(r.status_code)
    print(r.text)
    
register()
