"""
LearningStudio RESTful API Libraries 
These libraries make it easier to use the LearningStudio Course APIs.
Full Documentation is provided with the library. 

Need Help or Have Questions? 
Please use the PDN Developer Community at https://community.pdn.pearson.com

:category   LearningStudio Course APIs
:author     Wes Williams <wes.williams@pearson.com>
:author     Pearson Developer Services Team <apisupport@pearson.com>
:copyright  2014 Pearson Education Inc.
:license    http://www.apache.org/licenses/LICENSE-2.0  Apache 2.0
:version    1.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
service
-------

Defines the basic HTTP method wrappers and related utilities to be used by higher-level service objects.


"""

import copy
import json
import logging
import base64

from learningstudio.oauth.service import AuthMethod
from learningstudio.oauth.util import current_time_millis, unix_time_millis
from learningstudio.oauth.util import parse_url, parts_to_url, parse_xml_tag
from learningstudio.oauth.util import parse_url_and_connect, datetime_to_millis
from learningstudio.oauth.util import json_loads
from learningstudio.core.response import Response

class HttpStatusCode:
    """Declares HTTP status code constants.

    """
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_ERROR = 500

class DataFormat:
    """Declares constants that identifies the dataformats supported by the remote service calls.

    """
    JSON = 'JSON'
    XML = 'XML'

class BasicService(object):
    """Provides the base REST API client functionality for all user-level services like exams, grades and content.

    """

    API_DOMAIN = "https://api.learningstudio.com"
    __HTTP_METHODS = ('GET', 'PUT', 'POST', 'DELETE',)    
    __PATH_SYSTEMDATETIME = "/systemDateTime"

    def __getServiceIdentifier():
        return "LS-Library-Core-Python-V1"
    
    def __init__(self, oauth_service_factory):
        """Initializes a BasicService object.

        :param oauth_service_factory: The factory object used to create the authentication services.
        :type oauth_service_factory: :class:`learningstudio.oauth.service.OAuthServiceFactory`

        """
        self.__oauth_service_factory = oauth_service_factory
        self.__data_format = DataFormat.JSON
        self.__auth_method = AuthMethod.oauth1_signature_service()
        self.__username = None
        self.__password = None
        self.__current_oauth_request = None

    def doGet(self, relative_url, extra_headers = None, body = ''):
        """Makes a GET HTTP request.

        :param relative_url: The resource URL.
        :type relative_url: str
        :param extra_headers: Any additional HTTP headers to be send.
        :type extra_headers: dict
        :param body: Any request body to be send.
        :type body: str

        :returns: An object that encapsulates the HTTP response.
        :rtype: :class:`learningstudio.core.response.Response`

        """
        return self.doMethod('GET', relative_url, extra_headers = extra_headers,
                             body = body)

    def doPut(self, relative_url, extra_headers = None, body = ''):
        """Makes a PUT HTTP request.

        relative_url - The resource URL.
        extra_headers - Any additional HTTP headers to be send.
        body - Any request body to be send.

        Returns an object that encapsulates the HTTP response.
        """
        return self.doMethod('PUT', relative_url, extra_headers = extra_headers,
                             body = body)

    def doPost(self, relative_url, extra_headers = None, body = ''):
        """Makes a POST HTTP request.

        relative_url - The resource URL.
        extra_headers - Any additional HTTP headers to be send.
        body - Any request body to be send.

        Returns an object that encapsulates the HTTP response.
        """
        return self.doMethod('POST', relative_url, extra_headers = extra_headers,
                             body = body)

    def doDelete(self, relative_url, extra_headers = None, body = ''):
        """Makes a DELETE HTTP request.

        relative_url - The resource URL.
        extra_headers - Any additional HTTP headers to be send.
        body - Any request body to be send.

        Returns an object that encapsulates the HTTP response.
        """
        return self.doMethod('DELETE', relative_url, 
                             extra_headers = extra_headers,
                             body = body)

    def doMethod(self, http_method, relative_url, 
                 extra_headers = None, body = ''):
        """Makes a generic HTTP request.

        http_method - A string that identifies the request method.
        relative_url - The resource URL.
        extra_headers - Any additional HTTP headers to be send.
        body - Any request body to be send.

        Returns an object that encapsulates the HTTP response.
        """
        assert (http_method in BasicService.__HTTP_METHODS)
        if self.__data_format == DataFormat.XML: relative_url = BasicService.__append_extn(relative_url, '.xml')
        full_url = BasicService.API_DOMAIN + relative_url
        logging.debug('REQUEST - Method: %s, URL: %s, Body: %s.', http_method, full_url, body)
        oauth_headers = self.__get_oauth_headers(http_method, full_url, body)
        if oauth_headers == None: 
            raise RuntimeError('Authentication method not selected. SEE useOAuth# methods.')
        if extra_headers != None:
            for key in extra_headers.keys():
                value = extra_headers[key]
                if oauth_headers.get(key) == None:
                    oauth_headers[key] = value
                else:
                    raise RuntimeError('Extra headers can not include OAuth headers.')
        http_conn = None
        try:
            http_conn, _ = parse_url_and_connect(BasicService.API_DOMAIN)
            headers = copy.deepcopy(oauth_headers)
            headers["User-Agent"] = self.__getServiceIdentifier
            if (http_method == 'POST' or http_method == 'PUT') and len(body) > 0:
                byte_array = body.encode('utf-8')
                headers['Content-Type'] = 'application/json'
                headers['Content-Length'] = len(byte_array)
                http_conn.request(http_method, relative_url, byte_array, headers)
            else:
                http_conn.request(http_method, relative_url, None, headers)
            response = http_conn.getresponse()
            content_type = response.getheader('Content-Type', 'UNKNOWN')
            content = response.read();
            ctype = content_type.lower()
            is_binary = (ctype.find('text') == -1 and ctype.find('xml') == -1 and ctype.find('json') == -1)
            if is_binary:
                content = base64.b64decode(content)
            return Response(method = http_method, 
                            url = BasicService.API_DOMAIN + relative_url,
                            content = content,
                            content_type = content_type,
                            is_binary = is_binary,
                            status_code = response.status,
                            status_message = response.reason)                            
        finally:
            if http_conn != None:
                http_conn.close()

    def useOAuth1(self):
        """Sets-up the service to use OAuth1 authentication for further requests.

        """
        self.__auth_method = AuthMethod.oauth1_signature_service()
        self.__username = None
        self.__password = None
        self.__current_oauth_request = None

    def useOAuth2(self, username, password = None):
        """Sets-up the service to use OAuth2 authentication for further requests.
        
        """
        self.__username = username
        self.__current_oauth_request = None
        if password == None:
            self.__auth_method = AuthMethod.oauth2_assertion_service()
            self.__password = None
        else:
            self.__auth_method = AuthMethod.oauth2_password_service()
            self.__password = password            

    def destroy(self):
        """Invalidates the object.

        """

        self.__oauth_service_factory = None
        self.__data_format = None
        self.__auth_method = None
        self.__username = None
        self.__password = None
        self.__current_oauth_request = None

    def getPreferredFormat(self):
        """Returns the currently preferred response format.

        :returns: The preferred data format - either JSON or XML.
        :rtype: str

        """

        return self.__data_format

    def setPreferredFormat(self, fmt):
        """Sets the currently preferred response format.

        :param fmt: A string that identifies the format. Should be either `DataFormat.XML` or `DataFormat.JSON`.'
        :type fmt: str

        """
        self.__data_format = fmt

    def getSystemDateTime(self):
        """Returns the system time on the API server.
        
        :returns: The system time on the server.
        :rtype: str

        """
        return self.doMethod('GET', BasicService.__PATH_SYSTEMDATETIME)

    def getSystemDateTimeMillis(self):
        """Returns the system time on the API server as milliseconds.

        :returns: The system time on the server as milliseconds.
        :rtype: long

        """
        response = self.getSystemDateTime()
        if response.isError():
            raise IOError('Time lookup failed: %s - %s.' % (response.getStatusCode(), response.getStatusMessage()))
        content = response.getContent()
        time_value = None
        if self.__data_format == DataFormat.XML:
            time_value = parse_xml_tag(content, ['systemDateTime', 'value'])
        else:
            json_data = json_loads(content)
            time_value = json_data['systemDateTime']['value']
        return datetime_to_millis(time_value)
        
    def __get_oauth_headers(self, http_method, url, body):
        service = self.__oauth_service_factory.build(self.__auth_method)
        headers = {}
        if self.__auth_method == AuthMethod.oauth1_signature_service():
            request = service.generateRequest(http_method = http_method,
                                              url = url,
                                              body = body)
            headers = request.getHeaders()
        else: 
            if self.__current_oauth_request != None:
                if current_time_millis() >= self.__current_oauth_request.getExpirationTime():
                    logging.debug('Previous OAuth2 headers have expired.')
                    if self.__auth_method == AuthMethod.oauth2_password_service():
                        logging.debug('Refreshing oauth2 token.')
                        refresh_request = self.__current_oauth_request
                        self.__current_oauth_request = None
                        try:
                            self.__current_oauth_request = service.refreshOAuth2PasswordRequest(refresh_request)
                        except e:
                            logging.debug('Failed to refresh oauth2 token: ' + str(e))
                    else:
                        self.__current_oauth_request = None
            if self.__current_oauth_request == None:
                logging.debug('Generating new OAuth2 headers.')
                if self.__auth_method == AuthMethod.oauth2_password_service():
                    self.__current_oauth_request = service.generateRequest(username = self.__username,
                                                                           password = self.__password)
                elif self.__auth_method == AuthMethod.oauth2_assertion_service():
                    self.__current_oauth_request = service.generateRequest(username = self.__username)
                else:
                    raise NotImplementedError('Auth method ' + str(self.__auth_method) + ' is not implemented.')
            headers = self.__current_oauth_request.getHeaders()
        return copy.deepcopy(headers)
    
    @staticmethod
    def __append_extn(url, extn):
        parts = parse_url(url)
        return parts_to_url(parts.scheme, parts.netloc, parts.path + extn,
                            parts.params, parts.query, parts.fragment)
