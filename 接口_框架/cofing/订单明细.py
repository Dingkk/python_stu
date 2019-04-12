#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"

import requests

class dingdanmingxi(object):
    def mingxi(self,r,t):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'
        head = {'Content-Type':'application/json',
                    'x-dealer-code':'2100005',
                    'x-position-code':'D_PO_1028',
                    'x-resource-code':'pol4s_partOrderSearch_partOrderDetailSearch',
                    'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                    'x-user-code':'dhxc1u',
                    'x-access-token':'0da5606a534fa727dfd7f502df38be65'}
        b = '{ "pageNum": "%s","pgeSize": "%s","queryTerms": {"orderNo": "V2100880181219390"}}' %(r,t)
        b =b.encode('utf-8')
        res = requests.post(url,headers=head,data=b)
        return res.json()

if __name__=='__main__':
    aa = dingdanmingxi()
    a = aa.mingxi(1,10)
    print(a)