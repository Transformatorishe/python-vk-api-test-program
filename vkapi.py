import requests
import json

def main():
    ffile=open('token.txt','r')
    token=ffile.read()
    ffile.close()

    url='https://api.vk.com/method/wall.post'
    r=requests.get(url=url, params={'owner_id':'233025153',
                                    'message':'privet',
                                    'attachments':'photo419858248_457241760',
                                    'v': '5.52', 'access_token': token})
    print(r.text)
main()