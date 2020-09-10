# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from taifucloudcloud.common.exception.taifucloud_cloud_sdk_exception import TencentCloudSDKException
from taifucloudcloud.common.abstract_client import AbstractClient
from taifucloudcloud.gaap.v20180529 import models


class GaapClient(AbstractClient):
    _apiVersion = '2018-05-29'
    _endpoint = 'gaap.taifucloudcloudapi.com'


    def AddRealServers(self, request):
        """添加源站(服務器)訊息，支援IP或域名

        :param request: Request instance for AddRealServers.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.AddRealServersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.AddRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddRealServersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindListenerRealServers(self, request):
        """本介面（BindListenerRealServers）用于TCP/UDP監聽器綁定解綁源站。
        注意：本介面會解綁之前綁定的源站，綁定本次調用所選擇的源站。例如：原來綁定的源站爲A，B，C，本次調用的選擇綁定的源站爲C，D，E，那麽調用後所綁定的源站爲C，D，E。

        :param request: Request instance for BindListenerRealServers.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.BindListenerRealServersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.BindListenerRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindListenerRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindListenerRealServersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindRuleRealServers(self, request):
        """該介面用于7層監聽器的轉發規則綁定源站。注意：本介面會解綁之前綁定的源站，綁定本次調用所選擇的源站。

        :param request: Request instance for BindRuleRealServers.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.BindRuleRealServersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.BindRuleRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindRuleRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRuleRealServersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckProxyCreate(self, request):
        """本介面(CheckProxyCreate)用于查詢能否創建指定配置的加速通道。

        :param request: Request instance for CheckProxyCreate.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CheckProxyCreateRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CheckProxyCreateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckProxyCreate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckProxyCreateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseProxies(self, request):
        """本介面（CloseProxies）用于關閉通道。通道關閉後，不再産生流量，但每天仍然收取通道基礎配置費用。

        :param request: Request instance for CloseProxies.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CloseProxiesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CloseProxiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseProxies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseProxiesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseSecurityPolicy(self, request):
        """關閉安全策略

        :param request: Request instance for CloseSecurityPolicy.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CloseSecurityPolicyRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CloseSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseSecurityPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCertificate(self, request):
        """本介面（CreateCertificate）用于創建Gaap相關證書和配置文件，包括基礎認證配置文件，用戶端CA證書，服務器SSL證書，Gaap SSL證書以及源站CA證書。

        :param request: Request instance for CreateCertificate.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateCertificateRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDomain(self, request):
        """本介面（CreateDomain）用于創建HTTP/HTTPS監聽器的訪問域名，用戶端請求通過訪問該域名來請求後端業務。
        該介面僅支援version3.0的通道。

        :param request: Request instance for CreateDomain.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateDomainRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDomainErrorPageInfo(self, request):
        """定制域名指定錯誤碼的錯誤響應

        :param request: Request instance for CreateDomainErrorPageInfo.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateDomainErrorPageInfoRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateDomainErrorPageInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDomainErrorPageInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDomainErrorPageInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHTTPListener(self, request):
        """該介面（CreateHTTPListener）用于在通道實例下創建HTTP協議類型的監聽器。

        :param request: Request instance for CreateHTTPListener.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateHTTPListenerRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateHTTPListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHTTPListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHTTPListenerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHTTPSListener(self, request):
        """該介面（CreateHTTPSListener）用于在通道實例下創建HTTPS協議類型的監聽器。

        :param request: Request instance for CreateHTTPSListener.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateHTTPSListenerRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateHTTPSListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHTTPSListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHTTPSListenerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProxy(self, request):
        """本介面（CreateProxy）用于創建/複制一個指定配置的加速通道。當複制通道時，需要設置新通道的基本配置參數，并設置ClonedProxyId來指定被複制的通道。

        :param request: Request instance for CreateProxy.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateProxyRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateProxyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProxy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProxyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProxyGroup(self, request):
        """本介面（CreateProxyGroup）用于創建通道組。

        :param request: Request instance for CreateProxyGroup.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateProxyGroupRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateProxyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProxyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProxyGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProxyGroupDomain(self, request):
        """本介面（CreateProxyGroupDomain）用于創建通道組域名，并開啓域名解析。

        :param request: Request instance for CreateProxyGroupDomain.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateProxyGroupDomainRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateProxyGroupDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProxyGroupDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProxyGroupDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRule(self, request):
        """該介面（CreateRule）用于創建HTTP/HTTPS監聽器轉發規則。

        :param request: Request instance for CreateRule.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateRuleRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityPolicy(self, request):
        """創建安全策略

        :param request: Request instance for CreateSecurityPolicy.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateSecurityPolicyRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityRules(self, request):
        """添加安全策略規則

        :param request: Request instance for CreateSecurityRules.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateSecurityRulesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateSecurityRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTCPListeners(self, request):
        """該介面（CreateTCPListeners）用于批次創建單通道或者通道組的TCP協議類型的監聽器。

        :param request: Request instance for CreateTCPListeners.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateTCPListenersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateTCPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTCPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTCPListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUDPListeners(self, request):
        """該介面（CreateUDPListeners）用于批次創建單通道或者通道組的UDP協議類型的監聽器。

        :param request: Request instance for CreateUDPListeners.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.CreateUDPListenersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.CreateUDPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUDPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUDPListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCertificate(self, request):
        """本介面（DeleteCertificate）用于删除證書。

        :param request: Request instance for DeleteCertificate.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DeleteCertificateRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DeleteCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDomain(self, request):
        """本介面（DeleteDomain）僅适用于7層監聽器，用于删除該監聽器下對應域名及域名下的所有規則，所有已綁定源站的規則将自動解綁。

        :param request: Request instance for DeleteDomain.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DeleteDomainRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDomainErrorPageInfo(self, request):
        """删除域名的定制錯誤

        :param request: Request instance for DeleteDomainErrorPageInfo.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DeleteDomainErrorPageInfoRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DeleteDomainErrorPageInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDomainErrorPageInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDomainErrorPageInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteListeners(self, request):
        """該介面（DeleteListeners）用于批次删除通道或通道組的監聽器，包括4/7層監聽器。

        :param request: Request instance for DeleteListeners.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DeleteListenersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DeleteListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteProxyGroup(self, request):
        """本介面（DeleteProxyGroup）用于删除通道組。

        :param request: Request instance for DeleteProxyGroup.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DeleteProxyGroupRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DeleteProxyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProxyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProxyGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRule(self, request):
        """該介面（DeleteRule）用于删除HTTP/HTTPS監聽器的轉發規則。

        :param request: Request instance for DeleteRule.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DeleteRuleRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecurityPolicy(self, request):
        """删除安全策略

        :param request: Request instance for DeleteSecurityPolicy.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DeleteSecurityPolicyRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DeleteSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecurityRules(self, request):
        """删除安全策略規則

        :param request: Request instance for DeleteSecurityRules.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DeleteSecurityRulesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DeleteSecurityRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessRegions(self, request):
        """本介面（DescribeAccessRegions）用于查詢加速區域，即用戶端接入區域。

        :param request: Request instance for DescribeAccessRegions.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeAccessRegionsRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeAccessRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessRegionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessRegionsByDestRegion(self, request):
        """本介面（DescribeAccessRegionsByDestRegion）根據源站區域查詢可用的加速區域清單

        :param request: Request instance for DescribeAccessRegionsByDestRegion.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeAccessRegionsByDestRegionRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeAccessRegionsByDestRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessRegionsByDestRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessRegionsByDestRegionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCertificateDetail(self, request):
        """本介面（DescribeCertificateDetail）用于查詢證書詳情，包括證書ID，證書名字，證書類型，證書内容以及金鑰等訊息。

        :param request: Request instance for DescribeCertificateDetail.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeCertificateDetailRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeCertificateDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificateDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificateDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCertificates(self, request):
        """本介面（DescribeCertificates）用來查詢可以使用的證書清單。

        :param request: Request instance for DescribeCertificates.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeCertificatesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeCertificatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCountryAreaMapping(self, request):
        """本介面（DescribeCountryAreaMapping）用于獲取國家地區編碼映射表。

        :param request: Request instance for DescribeCountryAreaMapping.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeCountryAreaMappingRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeCountryAreaMappingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCountryAreaMapping", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCountryAreaMappingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDestRegions(self, request):
        """本介面（DescribeDestRegions）用于查詢源站區域，即源站服務器所在區域。

        :param request: Request instance for DescribeDestRegions.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeDestRegionsRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeDestRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDestRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDestRegionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDomainErrorPageInfo(self, request):
        """查詢目前定制域名的錯誤響應

        :param request: Request instance for DescribeDomainErrorPageInfo.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeDomainErrorPageInfoRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeDomainErrorPageInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainErrorPageInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainErrorPageInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDomainErrorPageInfoByIds(self, request):
        """根據定制錯誤ID查詢錯誤響應

        :param request: Request instance for DescribeDomainErrorPageInfoByIds.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeDomainErrorPageInfoByIdsRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeDomainErrorPageInfoByIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainErrorPageInfoByIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainErrorPageInfoByIdsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroupAndStatisticsProxy(self, request):
        """該介面爲内部介面，用于查詢可以獲取統計數據的通道組和通道訊息

        :param request: Request instance for DescribeGroupAndStatisticsProxy.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeGroupAndStatisticsProxyRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeGroupAndStatisticsProxyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupAndStatisticsProxy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupAndStatisticsProxyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroupDomainConfig(self, request):
        """本介面（DescribeGroupDomainConfig）用于獲取通道組域名解析配置詳情。

        :param request: Request instance for DescribeGroupDomainConfig.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeGroupDomainConfigRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeGroupDomainConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupDomainConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupDomainConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHTTPListeners(self, request):
        """該介面（DescribeHTTPListeners）用來查詢HTTP監聽器訊息。

        :param request: Request instance for DescribeHTTPListeners.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeHTTPListenersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeHTTPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHTTPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHTTPListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHTTPSListeners(self, request):
        """本介面（DescribeHTTPSListeners）用來查詢HTTPS監聽器訊息。

        :param request: Request instance for DescribeHTTPSListeners.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeHTTPSListenersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeHTTPSListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHTTPSListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHTTPSListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListenerRealServers(self, request):
        """該介面（DescribeListenerRealServers）用于查詢TCP/UDP監聽器源站清單，包括該監聽器已經綁定的源站清單以及可以綁定的源站清單。

        :param request: Request instance for DescribeListenerRealServers.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeListenerRealServersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeListenerRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListenerRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListenerRealServersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListenerStatistics(self, request):
        """該介面用于查詢監聽器統計數據，包括出入頻寬，出入包量，并發數據。支援300秒, 3600秒和86400秒的細粒度，取值爲細粒度範圍内最大值。

        :param request: Request instance for DescribeListenerStatistics.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeListenerStatisticsRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeListenerStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListenerStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListenerStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProxies(self, request):
        """本介面（DescribeProxies）用于查詢通道實例清單。

        :param request: Request instance for DescribeProxies.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxiesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxiesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProxiesStatus(self, request):
        """本介面（DescribeProxiesStatus）用于查詢通道狀态清單。

        :param request: Request instance for DescribeProxiesStatus.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxiesStatusRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxiesStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxiesStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxiesStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProxyAndStatisticsListeners(self, request):
        """該介面爲内部介面，用于查詢可以獲取統計數據的通道和監聽器訊息

        :param request: Request instance for DescribeProxyAndStatisticsListeners.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyAndStatisticsListenersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyAndStatisticsListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyAndStatisticsListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyAndStatisticsListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProxyDetail(self, request):
        """本介面（DescribeProxyDetail）用于查詢通道詳情。

        :param request: Request instance for DescribeProxyDetail.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyDetailRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProxyGroupDetails(self, request):
        """本介面（DescribeProxyGroupDetails）用于查詢通道組詳情。

        :param request: Request instance for DescribeProxyGroupDetails.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyGroupDetailsRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyGroupDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyGroupDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyGroupDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProxyGroupList(self, request):
        """本介面（DescribeProxyGroupList）用于拉取通道組清單及各通道組基本訊息。

        :param request: Request instance for DescribeProxyGroupList.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyGroupListRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyGroupListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProxyGroupStatistics(self, request):
        """該介面用于查詢監聽器統計數據，包括出入頻寬，出入包量，并發數據。支援300, 3600和86400的細粒度，取值爲細粒度範圍内最大值。

        :param request: Request instance for DescribeProxyGroupStatistics.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyGroupStatisticsRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyGroupStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyGroupStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyGroupStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProxyStatistics(self, request):
        """該介面用于查詢監聽器統計數據，包括出入頻寬，出入包量，并發，丢包和延遲數據。支援300, 3600和86400的細粒度，取值爲細粒度範圍内最大值。

        :param request: Request instance for DescribeProxyStatistics.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyStatisticsRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeProxyStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRealServerStatistics(self, request):
        """該介面（DescribeRealServerStatistics）用于查詢源站健康檢查結果的統計數據。源站狀态展示位爲1：正常或者0：異常。查詢的源站需要在監聽器或者規則上進行了綁定，查詢時需指定綁定的監聽器或者規則ID。該介面支援最近1，3，6，12，24小時内1分鍾細粒度的源站狀态統計數據展示。

        :param request: Request instance for DescribeRealServerStatistics.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRealServerStatisticsRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRealServerStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealServerStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealServerStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRealServers(self, request):
        """本介面（DescribeRealServers）用于查詢源站訊息，可以根據項目名查詢所有的源站訊息，此外支援指定IP機或者域名的源站模糊查詢。

        :param request: Request instance for DescribeRealServers.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRealServersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealServersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRealServersStatus(self, request):
        """本介面（DescribeRealServersStatus）用于查詢源站是否已被規則或者監聽器綁定

        :param request: Request instance for DescribeRealServersStatus.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRealServersStatusRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRealServersStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealServersStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealServersStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRegionAndPrice(self, request):
        """該介面（DescribeRegionAndPrice）用于獲取源站區域和頻寬梯度價格

        :param request: Request instance for DescribeRegionAndPrice.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRegionAndPriceRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRegionAndPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegionAndPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionAndPriceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourcesByTag(self, request):
        """本介面（DescribeResourcesByTag）用于根據标簽來查詢對應的資源訊息，包括通道，通道組和源站。

        :param request: Request instance for DescribeResourcesByTag.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeResourcesByTagRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeResourcesByTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourcesByTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourcesByTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleRealServers(self, request):
        """本介面（DescribeRuleRealServers）用于查詢轉發規則相關的源站訊息， 包括該規則可綁定的源站訊息和已綁定的源站訊息。

        :param request: Request instance for DescribeRuleRealServers.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRuleRealServersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRuleRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRuleRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRuleRealServersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRules(self, request):
        """本介面（DescribeRules）用于查詢監聽器下的所有規則訊息，包括規則域名，路徑以及該規則下所綁定的源站清單。當通道版本爲3.0時，該介面會返回該域名對應的高級認證配置訊息。

        :param request: Request instance for DescribeRules.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRulesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRulesByRuleIds(self, request):
        """本介面（DescribeRulesByRuleIds）用于根據規則ID拉取規則訊息清單。支援一個或者多個規則訊息的拉取。一次最多支援10個規則訊息的拉取。

        :param request: Request instance for DescribeRulesByRuleIds.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRulesByRuleIdsRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeRulesByRuleIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRulesByRuleIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRulesByRuleIdsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityPolicyDetail(self, request):
        """獲取安全策略詳情

        :param request: Request instance for DescribeSecurityPolicyDetail.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeSecurityPolicyDetailRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeSecurityPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityPolicyDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityRules(self, request):
        """本介面（DescribeSecurityRules）用于根據安全規則ID查詢安全規則詳情清單。支援一個或多個安全規則的查詢。一次最多支援20個安全規則的查詢。

        :param request: Request instance for DescribeSecurityRules.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeSecurityRulesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeSecurityRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTCPListeners(self, request):
        """該介面（DescribeTCPListeners）用于查詢單通道或者通道組下的TCP監聽器訊息。

        :param request: Request instance for DescribeTCPListeners.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeTCPListenersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeTCPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTCPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTCPListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUDPListeners(self, request):
        """該介面（DescribeUDPListeners）用于查詢單通道或者通道組下的UDP監聽器訊息

        :param request: Request instance for DescribeUDPListeners.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DescribeUDPListenersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DescribeUDPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUDPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUDPListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyProxies(self, request):
        """本介面（DestroyProxies）用于銷毀。通道銷毀後，不再産生任何費用。

        :param request: Request instance for DestroyProxies.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.DestroyProxiesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.DestroyProxiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyProxies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyProxiesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceCreateProxy(self, request):
        """本介面（InquiryPriceCreateProxy）用于創建加速通道詢價。

        :param request: Request instance for InquiryPriceCreateProxy.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.InquiryPriceCreateProxyRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.InquiryPriceCreateProxyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateProxy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateProxyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCertificate(self, request):
        """本介面（ModifyCertificate）用于修改監聽器下的域名對應的證書。該介面僅适用于version3.0的通道。

        :param request: Request instance for ModifyCertificate.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyCertificateRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCertificateAttributes(self, request):
        """本介面（ModifyCertificateAttributes）用于修改證書，包括證明名字以及證書内容。

        :param request: Request instance for ModifyCertificateAttributes.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyCertificateAttributesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyCertificateAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCertificateAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCertificateAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDomain(self, request):
        """本介面（ModifyDomain）用于監聽器下的域名。當通道版本爲3.0時，支援對該域名所對應的證書修改。

        :param request: Request instance for ModifyDomain.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyDomainRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyGroupDomainConfig(self, request):
        """本介面（ModifyGroupDomainConfig）用于配置通道組就近接入域名。

        :param request: Request instance for ModifyGroupDomainConfig.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyGroupDomainConfigRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyGroupDomainConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyGroupDomainConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyGroupDomainConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyHTTPListenerAttribute(self, request):
        """該介面（ModifyHTTPListenerAttribute）用于修改通道的HTTP監聽器配置訊息，目前僅支援修改監聽器的名稱。
        注意：通道組通道暫時不支援HTTP/HTTPS監聽器。

        :param request: Request instance for ModifyHTTPListenerAttribute.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyHTTPListenerAttributeRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyHTTPListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHTTPListenerAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHTTPListenerAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyHTTPSListenerAttribute(self, request):
        """該介面（ModifyHTTPSListenerAttribute）用于修改HTTPS監聽器配置，當前不支援通道組和v1版本通道。

        :param request: Request instance for ModifyHTTPSListenerAttribute.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyHTTPSListenerAttributeRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyHTTPSListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHTTPSListenerAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHTTPSListenerAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProxiesAttribute(self, request):
        """本介面（ModifyProxiesAttribute）用于修改實例的屬性（目前只支援修改通道的名稱）。

        :param request: Request instance for ModifyProxiesAttribute.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyProxiesAttributeRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyProxiesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProxiesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProxiesAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProxiesProject(self, request):
        """本介面（ModifyProxiesProject）用于修改通道所屬項目。

        :param request: Request instance for ModifyProxiesProject.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyProxiesProjectRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyProxiesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProxiesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProxiesProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProxyConfiguration(self, request):
        """本介面（ModifyProxyConfiguration）用于修改通道的配置。根據當前業務的容量需求，擴容或縮容相關通道的配置。僅支援Scalarable爲1的通道,Scalarable可通過介面DescribeProxies獲取。

        :param request: Request instance for ModifyProxyConfiguration.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyProxyConfigurationRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyProxyConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProxyConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProxyConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProxyGroupAttribute(self, request):
        """本介面（ModifyProxyGroupAttribute）用于修改通道組屬性，目前僅支援修改通道組名稱。

        :param request: Request instance for ModifyProxyGroupAttribute.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyProxyGroupAttributeRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyProxyGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProxyGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProxyGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRealServerName(self, request):
        """本介面（ModifyRealServerName）用于修改源站的名稱

        :param request: Request instance for ModifyRealServerName.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyRealServerNameRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyRealServerNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRealServerName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRealServerNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRuleAttribute(self, request):
        """本介面（ModifyRuleAttribute）用于修改轉發規則的訊息，包括健康檢查的配置以及轉發策略。

        :param request: Request instance for ModifyRuleAttribute.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyRuleAttributeRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyRuleAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRuleAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRuleAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityRule(self, request):
        """修改安全策略規則名

        :param request: Request instance for ModifySecurityRule.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifySecurityRuleRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifySecurityRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySecurityRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTCPListenerAttribute(self, request):
        """本介面（ModifyTCPListenerAttribute）用于修改通道實例下TCP監聽器配置，包括健康檢查的配置，調度策略。

        :param request: Request instance for ModifyTCPListenerAttribute.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyTCPListenerAttributeRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyTCPListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTCPListenerAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTCPListenerAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUDPListenerAttribute(self, request):
        """本介面（ModifyUDPListenerAttribute）用于修改通道實例下UDP監聽器配置，包括監聽器名稱和調度策略的修改。

        :param request: Request instance for ModifyUDPListenerAttribute.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.ModifyUDPListenerAttributeRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.ModifyUDPListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUDPListenerAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUDPListenerAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OpenProxies(self, request):
        """該介面（OpenProxies）用于開啓一條或者多條通道。

        :param request: Request instance for OpenProxies.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.OpenProxiesRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.OpenProxiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenProxies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenProxiesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OpenSecurityPolicy(self, request):
        """開啓安全策略

        :param request: Request instance for OpenSecurityPolicy.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.OpenSecurityPolicyRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.OpenSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenSecurityPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveRealServers(self, request):
        """删除已添加的源站(服務器)IP或域名

        :param request: Request instance for RemoveRealServers.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.RemoveRealServersRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.RemoveRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveRealServersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetAuthentication(self, request):
        """本介面（SetAuthentication）用于通道的高級認證配置，包括認證方式選擇，以及各種認證方式對應的證書選擇。僅支援Version3.0的通道。

        :param request: Request instance for SetAuthentication.
        :type request: :class:`taifucloudcloud.gaap.v20180529.models.SetAuthenticationRequest`
        :rtype: :class:`taifucloudcloud.gaap.v20180529.models.SetAuthenticationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetAuthentication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetAuthenticationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)