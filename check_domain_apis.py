import requests
#Tencent import
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.domain.v20180808 import domain_client, models

#ALiCloud import
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkdomain.request.v20180129.CheckDomainRequest import CheckDomainRequest

# check_domain_ali中参数region的可选值,根据你的位置选择
# 华东1（杭州）	cn-hangzhou
# 华东2（上海）	cn-shanghai
# 华北1（青岛）	cn-qingdao
# 华北2（北京）	cn-beijing
# 华南1（深圳）	cn-shenzhen
# 新加坡	ap-southeast-1
# 马来西亚（吉隆坡）	ap-southeast-3
# 印度尼西亚（雅加达）	ap-southeast-5
# 日本（东京）	ap-northeast-1
# 英国（伦敦）	eu-west-1




def check_domain_ali(access_key_id,access_secret,region,domian_name):
    client = AcsClient(access_key_id,access_secret,region)
    request = CheckDomainRequest()
    request.set_accept_format('json')

    request.set_DomainName(domian_name)

    response = client.do_action_with_exception(request)
    # python2:  print(response) 
    print(str(response, encoding='utf-8'))
    return response

def check_domian_tencent(secret_id,secret_key,domian_name):
    try: 
        cred = credential.Credential(secret_id, secret_key) 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "domain.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = domain_client.DomainClient(cred, "", clientProfile) 

        req = models.CheckDomainRequest()
        params = {
            'DomainName':domian_name
        }
        req.from_json_string(json.dumps(params))

        resp = client.CheckDomain(req) 
        return resp

    except TencentCloudSDKException as err: 
        print(err)
        return None

#经检测这个借口异常的慢,且貌似直接对未注册域名返回错误
def check_domian_apitools(domian_name):
    url = 'https://api.devopsclub.cn/api/whoisquery?domain='+domian_name+'&type=json&standard=true'
    #args = '?domain=domian_name

    response = requests.post(url)
    return response
    
if __name__=='__main__':
    test_domain_name = 'zongdiu.com'
    response_tencent = check_domian_tencent('AKIDdY3NRuRVlm0v2tCndGdkTuB95KKBsmW1','Scx3ycFJBnBqHTOL9yYw28E7jBbYEjyz',test_domain_name)
    print(response_tencent)
    response_ali = check_domain_ali('LTAI4G2BFyMDH5LncfK1cdXD', 'X3y4RO8lh8wnbumHvyADN2ETYmT4qY', 'cn-hangzhou',test_domain_name)
    response_apitools = check_domian_apitools('asfdfafweef.com')
    print(response_apitools.text)