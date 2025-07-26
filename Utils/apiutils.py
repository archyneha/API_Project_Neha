'''
In a test automation framework, a utils (short for utilities) file
or package typically contains reusable helper functions, classes,
or constants that support your test execution but don’t directly belong
to test cases, test data, or page objects.

To promote code reusability, modularity, and maintainability by avoiding
repetitive code in test scripts or framework core logic.

headers is passed to help the server understand what kind of response
the client (like a browser or script) expects.
'''
import requests, json

def getApiData(url, opHeader=None):
    headers={'Content-type':'application/json'}
    headers=(headers|opHeader) if isinstance(opHeader,dict) else headers
    response=requests.get(url,verify=False, headers=headers)
    print("\nRequestURL:"+url)
    print("request header:",response.request.headers)
    print("response header:",response.headers)
    return response

def postApiData(url,body):
    headers = {'Content-type': 'application/json'}
    print("\nReqURL:"+ url)
    #print("ReqBody:" +json.loads(body))
    r=requests.post(url, verify=False, json=body,headers=headers)
    return r

def delAPiData(url,body,opHeader=None):
    headers = {'Content-type': 'application/json'}
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    response=requests.delete(url,json=body,headers=headers)
    print("response====",response.text)
    print("headers===",headers)
    return response