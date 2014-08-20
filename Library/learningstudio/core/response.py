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
response
--------

Defines a class that represents the API server HTTP response.


"""

class Response:
    """An object of this class wraps up an API server HTTP response.

    """

    def __init__(self, method, url,
                 content, content_type,
                 is_binary, status_code, 
                 status_message):
        """Initializes a Response object.

        :param method: Identifies the HTTP method for which the response was generated.
        :type method: str
        :param url: The resource request that generated this response.
        :type url: str
        :param content: The response content.
        :type content: str
        :param content_type: The MIME type of the content.
        :type content_type: str
        :param is_binary: A flag that denotes whether the content is in textual or binary format.
        :type is_binary: bool
        :param status_code: The HTTP status code of the response.
        :type status_code: int
        :param status_message: The HTTP status message of the response.
        :type status_message: str

        """
        self.__method = method
        self.__url = url
        self.__content = content
        self.__content_type = content_type
        self.__is_binary = is_binary
        self.__status_code = status_code
        self.__status_message = status_message

    def getMethod(self): 
        """Returns the HTTP method that generated this response.

        :returns: An HTTP method like GET, PUT or POST.
        :rtype: str

        """
        return self.__method

    def getUrl(self): 
        """Returns the resource URL that generated this response.

        :returns: A resource URL
        :rtype: str

        """
        return self.__url

    def getContent(self): 
        """Returns the text content of the response. If the content is binary, returns `None`.

        :returns: The text content of the response or `None`.
        :rtype: str or None.

        """
        if self.__is_binary: return None
        if type(self.__content) is bytes:
            self.__content = self.__content.decode(encoding = 'UTF-8')
        return self.__content

    def getBinaryContent(self): 
        """Returns the binary content of the response. If the content is textual, returns `None`.

        :returns: The binary content of the response or `None`.
        :rtype: str or None.

        """
        return self.__content if self.__is_binary else None

    def getContentType(self): 
        """Returns the MIME type of the content.

        :returns: A MIME type identifier.
        :rtype: str

        """
        return self.__content_type

    def isBinaryContent(self): 
        """Returns `True` if the content is binary.

        :returns: Returns `True` if the content is binary.
        :rtype: bool

        """
        return self.__is_binary

    def getStatusCode(self): 
        """Returns the HTTP status code of the response.

        :returns: An HTTP status code.
        :rtype: int
        
        """
        return self.__status_code

    def getStatusMessage(self): 
        """Returns the HTTP status message of the response.

        :returns: An HTTP status message.
        :rtype: str

        """
        return self.__status_message

    def setContent(self, content):
        """Updates the content field of the response.

        :param content: The new content.
        :type content: str

        """
        self.__content = content

    def setStatusCode(self, status_code):
        """Updates the HTTP status code of the response.

        :param status_code: New status code.
        :type status_code: int

        """
        self.__status_code = status_code

    def isError(self): 
        """Returns `True` if the status code falls in the range of HTTP error codes.

        :returns: `True` if the status code denotes an HTTP error.
        :rtype: bool

        """
        return (self.__status_code < 200 or self.__status_code >= 300)

    def __repr__(self):
        return 'Method: %s, URL: %s, Code: %s, Message: %s, ContentType: %s, Content: %s'\
            % (self.__method, self.__url, self.__status_code, self.__status_message,
               self.__content_type, self.__content)
