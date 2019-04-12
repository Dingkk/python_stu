#!/user/bin/python
# -*- coding:utf-8 -*-
#接口，请求传参和结果对比
#http协议  用requests
import requests
import json
import unittest

url='https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData'
head={
    'Content-Type':'application/json',
    'x-dealer-code':'2100150',
    'x-position-code':'D_PO_1028',
    'x-resource-code':'BASIC_DATA',
    'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
    'x-user-code':'djy0mx',
    'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb',
}
body='{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
res=requests.post(url,headers=head,data=body)
# print(res.text)
mes=json.loads(res.text)
#或者可写mes=res.json()
print(mes['data']['applicationType'][0]['name'])
#断言
assert mes['data']['applicationType'][0]['name'] == '多装'
assert mes['data']['applicationType'][0]['value'] == '1'

unittest      #单元测试框架
#主要是对用例进行管理，执行