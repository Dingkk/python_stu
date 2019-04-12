#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"

import requests

class shouye(object):
    def shouyezhuangtai(self):
        url= "https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderHomePage"
        head={'Content-Type':'application/json','x-dealer-code':'2100005','x-position-code':'D_PO_1028','x-resource-code':'pol4s_partOrder_orderHomePage','x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394','x-user-code':'dhxc1u','x-access-token':'0da5606a534fa727dfd7f502df38be65'}
        res = requests.post(url, headers=head)
        return res.json()

if __name__ == '__main__':
    ss=shouye()
    a = ss.shouyezhuangtai()
    print(a)