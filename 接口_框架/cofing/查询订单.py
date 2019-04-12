#!/usr/bin/python
#-*- coding:utf-8 -*-
Author: "Ding kk"

import requests
class chaxun(object):
    def chaxundingdan(self,o,p):
        url= "https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList"
        head = {'Content-Type':'application/json',
                    'x-dealer-code':'2100005',
                    'x-position-code':'D_PO_1028',
                    'x-resource-code':'pol4s_partOrder_orderList',
                    'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
                    'x-user-code':'dhxc1u',
                    'x-access-token':'0da5606a534fa727dfd7f502df38be65'}
        b = '{"pageNum": %s,"pageSize": %s,"queryTerms": {"orderType": "","orderStatus": "","orderDelayFlag":"","orderNo": "","startReportDate": "","endReportDate": ""}}' %(o,p)
        b = b.encode('utf-8')
        res = requests.post(url,headers=head,data=b)
        return res.json()

if __name__=='__main__':
    gg = chaxun()
    a = gg.chaxundingdan(1,10)
    print(a)