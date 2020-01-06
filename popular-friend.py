import requests
import json
import time

ffile=open('token.txt','r')
token=ffile.read()
ffile.close()
url='https://api.vk.com/method/friends.get'

def main(url, token, id):
    r=requests.get(url=url, params={'user_id': id , 'v': '5.52', 'access_token': token})
    friends=json.loads(r.text)['response']
    return friends

frcount=0
fr=''
b=main(url,token,'419858248')['items']
for i in b:
    k=main(url,token,str(i))['count']
    if k>frcount:
        frcount=k
        fr=i
    print(i,'  ',k)
    time.sleep(10)

r=requests.get(url='https://api.vk.com/method/users.get', params={'user_id': fr ,
'v': '5.52',
'access_token': token})
name=json.loads(r.text)['response'][0]['last_name']+json.loads(r.text)['response'][0]['first_name']
print(name, frcount)
