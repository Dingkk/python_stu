#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Dingkk"

import requests

class suopeidingdan(object):
    def Dingdan(self,q,w):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/queryApplication'
        head ={'Content-Type':'application/json',
                'x-dealer-code':'2100150',
                'x-position-code':'D_PO_1028',
                'x-resource-code':'QUERY_APPLICATION',
                'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                'x-user-code':'djy0mx',
                'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
        ba = '{"pageNum": %s,"pageSize": %s,"orderByField":"","orderByrule":"","status":"","applicationType":"","applicationMode":"","applicationNo":"","partCode":"","applicationStartDate":"","applicationEndDate":""}' %(q,w)
        ba= ba.encode('utf-8')
        res=requests.post(url,headers=head,data=ba)
        return res.json()

if __name__=='__main__':
    ss = suopeidingdan()
    a = ss.Dingdan(10,1)
    print(a)