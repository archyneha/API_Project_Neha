import pytest
import random
import allure
import time
from Utils.myconfigparser import getFlaskAppBaseURL,getJsonFromFile
from Utils.apiutils import postApiData,delAPiData
baseURL=getFlaskAppBaseURL()
regUrlPath='register'
loginURLPath='login'
delUrlPath='delete'
registerJsonFile='registerApiValid.json'
randNum=random.randint(0,1000)
eMail='autoamteUser@auto'+str(randNum)
password='1234'

@pytest.fixture
def reg_user():
    payload=getPayloadDict_RegAPI(eMail,password)
    print(payload)
    regurl=baseURL+regUrlPath
    reg_response=postApiData(regurl, payload)
    print("reg_response=",reg_response)
    assert reg_response.status_code==201
    assert reg_response.json()['id']
    data=reg_response.json()
    yield data # anything after this statement will run as tear down or after the test function is executed
    print("***** After Yield *****")
    time.sleep(30)
    delUrl=baseURL+delUrlPath
    loginUrl=baseURL+loginURLPath
    login_resp=postApiData(loginUrl,payload)
    token=login_resp.json()['token']
    headers={'x-access-token':token}
    payload={"id":reg_response.json()['id']}
    del_resp=delAPiData(delUrl,payload,headers)
    print("del_resp==",del_resp.text)
    assert del_resp.status_code==200
    assert del_resp.json()['id']==reg_response.json()['id']


def test_loginCorrectCreds(reg_user):
    payload=getPayloadDict_RegAPI(eMail, password)
    url=baseURL+loginURLPath
    resp=postApiData(url, payload)
    assert resp.status_code==200




def getPayloadDict_RegAPI(email=None,pwd=None):
    payload=getJsonFromFile(registerJsonFile)
    payload['email']=email
    payload['password']=pwd
    return payload

