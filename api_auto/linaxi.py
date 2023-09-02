# -*- coding: utf-8 -*-
"""
@Time:2023/9/2 10:06
@Auth:kirosbaby
@QQ:308902181
"""
import requests

url = 'https://cc.163.com/category/?format=json'

resp = requests.get(url=url)
for i in resp.json()['game_list']:
    print(i['gamename'])
# print(resp.json()['game_list'][1]['gamename'])
