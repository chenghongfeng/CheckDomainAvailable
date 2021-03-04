import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.domain.v20180808 import domain_client, models

def CheckDomianTencent(domian_name):
    secret_id = 'AKIDv4B3e0dq0ste7JE2h7FK0QbkhRuFcAj0'
    secret_key = 'twlKegjUDn9F4comZ6TBemcBhygRzGFz'
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

available = CheckDomianTencent('chenghongfeng.com').Available;
if(available):
    print('OK')
