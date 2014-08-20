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

Defines a class that implements :class:`learningstudio.core.service.BasicService` for the Content API.


"""

import json
from learningstudio.core.service import BasicService, HttpStatusCode
from learningstudio.oauth.util import json_loads

PATH_COURSES_ITEMS = '/courses/%s/items'
PATH_COURSES_ITEMS_ = '/courses/%s/items/%s'
PATH_COURSES_ITEMHIERARCHY = '/courses/%s/itemHierarchy'
PATH_COURSES_TEXTMULTIMEDIAS = '/courses/%s/textMultimedias'
PATH_COURSES_TEXTMULTIMEDIAS__CONTENTPATH_ = '/courses/%s/textMultimedias/%s/%s'
PATH_COURSES_TEXTMULTIMEDIAS__CONTENTPATH__USESOURCEDOMAIN = '/courses/%s/textMultimedias/%s/%s?useSourceDomain=true'
PATH_COURSES_TEXTMULTIMEDIAS_ = '/courses/%s/textMultimedias/%s'
PATH_COURSES_MSOFFICEDOCUMENTS = '/courses/%s/msOfficeDocuments'
PATH_COURSES_MSOFFICEDOCUMENTS_ = '/courses/%s/msOfficeDocuments/%s'
PATH_COURSES_MSOFFICEDOCUMENTS_ORIGINALDOCUMENT = '/courses/%s/msOfficeDocuments/%s/originalDocument'
PATH_COURSES_MSOFFICEDOCUMENTS_CONTENT_ = '/courses/%s/msOfficeDocuments/%s/content/%s'
PATH_COURSES_WEBCONTENTUPLOADS = '/courses/%s/webContentUploads'
PATH_COURSES_WEBCONTENTUPLOADS_ = '/courses/%s/webContentUploads/%s'
PATH_COURSES_WEBCONTENTUPLOADS_ORIGINALDOCUMENT = '/courses/%s/webContentUploads/%s/originalDocument'
PATH_COURSES_WEBCONTENTUPLOADS_CONTENT_ = '/courses/%s/webContentUploads/%s/content/%s'

PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSEHIEARCHY = '/courses/%s/threadedDiscussions/%s/topics/%s/responseHierarchy'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEHIEARCHY = '/courses/%s/threadedDiscussions/%s/topics/%s/responses/%s/responseHierarchy'
PATH_USERS_COURSES_ITEMS = '/users/%s/courses/%s/items'
PATH_USERS_COURSES_ITEMHIERARCHY = '/users/%s/courses/%s/itemHierarchy'
PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES_USERVIEWRESPONSES = '/users/%s/courses/%s/threadedDiscussions/%s/topics/%s/userviewresponses/%s/userviewresponses'
PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES_USERVIEWRESPONSES__DEPTH = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES_USERVIEWRESPONSES + '?depth=%s'
PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES = '/users/%s/courses/%s/threadedDiscussions/%s/topics/%s/userviewresponses'
PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES__DEPTH = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES + '?depth=%s'

PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSECOUNTS = '/users/%s/courses/%s/threadedDiscussions/%s/topics/%s/responses/%s/responseCounts'
PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSECOUNTS__DEPTH = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSECOUNTS + '?depth=%s'
PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSECOUNTS = '/users/%s/courses/%s/threadedDiscussions/%s/topics/%s/responseCounts'
PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSECOUNTS__DEPTH = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSECOUNTS + '?depth=%s'

PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEBRANCH = '/courses/%s/threadedDiscussions/%s/topics/%s/responses/%s/responseBranch'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEAUTHOR = '/courses/%s/threadedDiscussions/%s/topics/%s/responses/%s/responseAuthor'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEANDAUTHORCOMPS = '/courses/%s/threadeddiscussions/%s/topics/%s/responses/%s/responseAndAuthorComps'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEANDAUTHORCOMPS__DEPTH = '/courses/%s/threadedDiscussions/%s/topics/%s/responses/%s/responseAndAuthorComps?depth=%s'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSEANDAUTHORCOMPS = '/courses/%s/threadedDiscussions/%s/topics/%s/responseAndAuthorComps'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSEANDAUTHORCOMPS__DEPTH = '/courses/%s/threadedDiscussions/%s/topics/%s/responseAndAuthorComps?depth=%s'

PATH_USERS_COURSES_THREADEDDISCUSSIONS__LASTRESPONSE = '/users/%s/courses/%s/threadedDiscussions/lastResponse'
PATH_COURSES_THREADEDDISCUSSIONS = '/courses/%s/threadedDiscussions'
PATH_COURSES_THREADEDDISCUSSIONS__USESOURCEDOMAIN = '/courses/%s/threadedDiscussions?UseSourceDomain=true'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS = '/courses/%s/threadedDiscussions/%s/topics'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS__USESOURCEDOMAIN = '/courses/%s/threadedDiscussions/%s/topics?UseSourceDomain=true'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_ = '/courses/%s/threadedDiscussions/%s/topics/%s'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_USESOURCEDOMAIN = '/courses/%s/threadedDiscussions/%s/topics/%s?UseSourceDomain=true'

PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSE_READSTATUS = '/users/%s/courses/%s/threadedDiscussions/%s/topics/%s/responses/%s/readStatus'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSES = '/courses/%s/threadedDiscussions/%s/topics/%s/responses/%s/responses'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_ = '/courses/%s/threadedDiscussions/%s/topics/%s/responses/%s'
PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES = '/courses/%s/threadedDiscussions/%s/topics/%s/responses'

class ContentService(BasicService):
    """An implementation of BasicService for handling the Contents API.

    """

    def __init__(self, oauth_service_factory):
        super(ContentService, self).__init__(oauth_service_factory)
        
    def __getServiceIdentifier():
        return "LS-Library-Content-Python-V1"

    def getItems(self, courseId):
        """Get items for a course with
        ``GET /courses/{courseId}/items``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_ITEMS % (courseId,)
        return self.doGet(relativeUrl)

    def getItem(self, courseId, itemId):
        """Get a specific item for a course with
        ``GET /courses/{courseId}/items/{itemId}``
        using OAuth1 or OAuth2.
        
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_ITEMS_ % (courseId, itemId,)
        return self.doGet(relativeUrl)
    
    def getItemContent(self, courseId, itemId):
        """Get content for a specific item in a course with
        ``getItem(courseId, itemId)``
        by following the links to the item itself
        and next to the contentUrl
        
        :param courseId: ID of the course.
        :type courseId: str
        :param itemId: ID of the content item.
        :type itemId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.
        
        """
        # get the item details
        response = self.getItem(courseId, itemId)
        if response.isError():
            return response

        itemsJson = response.getContent()
        json_data = json_loads(itemsJson)
        
        # link to the item is in the link where title is null
        items = json_data.get('items')
        links = items[0]['links']
        for link in links:
            if link.get('title') is None:
                relativeUrl = self.__getRelativePath(link['href'])
        
        # get the item
        response = self.doGet(relativeUrl)
        if response.isError():
            return response
        
        itemJson = response.getContent()
        json_data = json_loads(itemJson)
        
        # get the item content location
        contentType, contentPath = json_data.popitem()
        relativeUrl = self.__getRelativePath(contentPath[0]['contentUrl'])
        
        # get and return the item content
        return self.doGet(relativeUrl)
        

    def getItemHierarchy(self, courseId):
		"""Get item hierarchy for a course with
		``GET /courses/{courseId}/itemHierarchy``
		using OAuth1 or OAuth2 as a teacher, teaching assistant, or administrator
		
		:param courseId: ID of the course.
        :type courseId: str
		
		:returns: A :class:`learningstudio.core.Response` object with details of status and content.
		"""
		
		relativeUrl = PATH_COURSES_ITEMHIERARCHY % (courseId,)
		return self.doGet(relativeUrl)

    def getUserItemHierarchy(self, userId, courseId):
		"""Get user item hierarchy for a course with
		``GET /users/{userId}/courses/{courseId}/itemHierarchy``
		using OAuth1 or OAuth2 as a teacher, teaching assistant, or administrator
		
		:param courseId: ID of the course.
        :type courseId: str
		
		:returns: A :class:`learningstudio.core.Response` object with details of status and content.
		"""
		
		relativeUrl = PATH_USERS_COURSES_ITEMHIERARCHY % (userId, courseId,)
		return self.doGet(relativeUrl)

    def getUserItems(self, userId, courseId):
        """Get user items in a course with
        ``GET /users/{userId}/courses/{courseId}/items``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type courseId: str
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_ITEMS % (userId, courseId,)
        return self.doGet(relativeUrl)
    
    def getItemLinkDetails(self, courseId, itemId):
        """Get links details from a specific item for a course with
        ``GET /courses/{courseId}/items/{itemId}``
        using OAuth2 as a student, teacher or teaching assistant.
        
        Example JSON structure: (Multimedia item)::
        
            { "details": 
               { "access": {...}, 
                 "schedule": {...}, 
                 "self": {...},
                 "selfType": "textMultimedias"
               }
            }
        
        :param courseId: ID of the course.
        :type courseId: str
        :param itemId: ID of the item.
        :type itemId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        response = self.getItem(courseId, itemId)
        if response.isError(): return response
        
        courseItemsJson = response.getContent()
        json_data = json_loads(courseItemsJson)
        items = json_data.get('items')
        detail = {}
            
        if items != None and len(items) > 0:
            for item in items:
                links = item.get('links')
                for link in links:
                    relativeUrl = self.__getRelativePath(link.get('href'))
                    response = self.doGet(relativeUrl)
                    if (response.isError()): return response
                    
                    linkElement = json_loads(response.getContent())
                    title = link.get('title')
                    if title == None:
                        if linkElement != None and len(linkElement) > 0:
                            for key in linkElement.keys():
                                value = linkElement[key]
                                detail['self'] = value
                                detail['selfType'] = key
                                break
                    else:
                        linkElement = linkElement.get(title)
                        detail[title] = linkElement
                            
            detailWrapper = {'details': detail}
            response.setContent(json.dumps(detailWrapper))
        else:
            raise RuntimeError('Unexpected condition in library: No items')
        return response
	
    def getTextMultimedias(self, courseId):
        """Get text multimedias by course with
        ``GET /courses/{courseId}/textMultimedias``
        using OAuth2 as a student, teacher or teaching assistant.
            
        :param courseId: ID of the course.
        :type courseId: str
        :param itemId: ID of the item.
        :type itemId: str
    
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_TEXTMULTIMEDIAS % (courseId,)
        return self.doGet(relativeUrl)
        
    def getTextMultimedia(self, courseId, textMediaId):
        """Get specific text multimedia content by course with
        ``GET /courses/{courseId}/textMultimedias``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param textMediaId: ID of the text media.
        :type textMediaId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_TEXTMULTIMEDIAS_ % (courseId, textMediaId,)
        return self.doGet(relativeUrl)
    
    def getTextMultimediasContent(self, courseId, textMediaId, contentPath = None):
        """Get specific text multimedia content by course with UseSourceDomain parameter with
        ``GET /courses/{courseId}/textMultimedias`` and 
        ``GET /courses/{courseId}/textMultimedias?UseSourceDomain=true``
        using OAuth2 as a student, teacher or teaching assistant
        
        :param courseId: ID of the course.
        :type courseId: str
        :param itemId: ID of the item.
        :type itemId: str
        :param contentPath: Path of content.
        :type contentPath: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content

        """
        if contentPath != None:
		    return self.__getTextMultimediasContent(courseId, textMediaId, contentPath)
            
        response = self.getTextMultimedia(courseId, textMediaId)
        if response.isError(): return response
        
        json_data = json_loads(response.getContent())
        json_data = json_data.get('textMultimedias')[0]
        contentUrl = json_data.get('contentUrl')
        relativeUrl = self.__getRelativePath(contentUrl)
        return self.doGet(relativeUrl)
        
        #if use_source_domain != None:
        #    return self.__getTextMultimediasContent(courseId, textMediaId, contentPath, use_source_domain)
        #else:
        #    relativeUrl = PATH_COURSES_TEXTMULTIMEDIAS__CONTENTPATH_ % (courseId, textMediaId, contentPath,)
        #    return self.doGet(relativeUrl)
        
    def __getTextMultimediasContent(self, courseId, textMediaId, contentPath):
        """Get specific text multimedia content by course with UseSourceDomain parameter with
        ``GET /courses/{courseId}/textMultimedias`` and 
        ``GET /courses/{courseId}/textMultimedias?UseSourceDomain=true``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course
        :type courseId: str
        :param itemId: ID of the item.
        :type itemId: str
        :param contentPath: Path of content.
        :type contentPath: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_TEXTMULTIMEDIAS__CONTENTPATH_ % (courseId, textMediaId, contentPath,)
        return self.doGet(relativeUrl)

    def getMsOfficeDocuments(self, courseId):
        """Get all MS Office documents in a course with
        ``GET /courses/{courseId}/msOfficeDocuments``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_MSOFFICEDOCUMENTS % (courseId,)
        return self.doGet(relativeUrl)
	
    def getMsOfficeDocument(self, courseId, msOfficeDocumentId):
        """Get a specific MS Office document in a course with
        ``GET /courses/{courseId}/msOfficeDocuments/{msOfficeDocumentId}``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param msOfficeDocumentId: ID of the ms office document.
        :type msOfficeDocumentId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_MSOFFICEDOCUMENTS_ % (courseId, msOfficeDocumentId,)
        return self.doGet(relativeUrl)
	
    def getMsOfficeDocumentContent(self, courseId, msOfficeDocumentId, content_path = None):
        """Get content for a specific MS Office Document in a course with
        ``GET /courses/{courseId}/msOfficeDocuments/{msOfficeDocumentId}`` and 
        ``GET /courses/{courseId}/msOfficeDocuments/{msOfficeDocumentId}/content/{contentPath}``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param msOfficeDocumentId: ID of the ms office document.
        :type msOfficeDocumentId: str
        :key content_path: Path of the content.
        :type content_path: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if content_path != None:
            return self.__getMsOfficeDocumentContent(courseId, msOfficeDocumentId, content_path)
            
        response = self.getMsOfficeDocument(courseId, msOfficeDocumentId)
        if response.isError(): return response
        
        json_data = json_loads(response.getContent())
        json_data = json_data.get('msOfficeDocuments')[0]
        contentUrl = json_data.get('contentUrl')
        relativeUrl = self.__getRelativePath(contentUrl)
        return self.doGet(relativeUrl)
        
    def __getMsOfficeDocumentContent(self, courseId, msOfficeDocumentId, contentPath):
        """Get content for a specific MS Office Document in a course with
        ``GET /courses/{courseId}/msOfficeDocuments/{msOfficeDocumentId}`` and 
        ``GET /courses/{courseId}/msOfficeDocuments/{msOfficeDocumentId}/content/{contentPath}``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param msOfficeDocumentId: ID of the ms office document.
        :type msOfficeDocumentId: str
        :param contentPath: Path of the content.
        :type contentPath: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_MSOFFICEDOCUMENTS_CONTENT_ % (courseId, msOfficeDocumentId, contentPath,)
        return self.doGet(relativeUrl)

    def getMsOfficeDocumentOriginal(self, courseId, msOfficeDocumentId):
        """Get the original of a specific MS Office document in a course with
        ``GET /courses/{courseId}/msOfficeDocuments/{msOfficeDocumentId}/originalDocument``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param msOfficeDocumentId: ID of the ms office document.
        :type msOfficeDocumentId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_MSOFFICEDOCUMENTS_ORIGINALDOCUMENT % (courseId, msOfficeDocumentId,)
        return self.doGet(relativeUrl)
	
    def getWebContentUploads(self, courseId):
        """Get all web content uploads in a course with
        ``GET /courses/{courseId}/webContentUploads``
        using OAuth2 as a student, teacher or teaching assistant
        
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_WEBCONTENTUPLOADS % (courseId,)
        return self.doGet(relativeUrl)
	
    def getWebContentUpload(self, courseId, webContentUploadId):
        """Get a specific MS Office document in a course with
        ``GET /courses/{courseId}/webContentUploads/{webContentUploadId}``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param webContentUploadId: ID of the ms office document.
        :type webContentUploadId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_WEBCONTENTUPLOADS_ % (courseId, webContentUploadId,)
        return self.doGet(relativeUrl)
	
    def getWebContentUploadOriginal(self, courseId, webContentUploadId):
        """Get a specific MS Office document in a course with
        ``GET /courses/{courseId}/webContentUploads/{webContentUploadId}``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param webContentUploadId: ID of the ms office document.
        :type webContentUploadId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_WEBCONTENTUPLOADS_ORIGINALDOCUMENT % (courseId, webContentUploadId,)
        return self.doGet(relativeUrl)

    def getWebContentUploadContent(self, courseId, webContentUploadId, content_path = None):
        """Get content for a specific Web Content Upload in a course with
        ``GET /courses/{courseId}/webContentUpload/{webContentUploadId}`` and
        ``GET /courses/{courseId}/webContentUpload/{webContentUploadId}/content/{contentPath}``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param webContentUploadId: ID of the web content upload.
        :type webContentUploadId: str
        :key content_path: Path of the content.
        :type content_path: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if content_path != None: return self.__getWebContentUploadContent(courseId, webContentUploadId, content_path)

        response = self.getWebContentUpload(courseId, webContentUploadId)
        if response.isError(): return response
		
        json_data = json_loads(response.getContent())
        json_data = json_data.get('webContentUploads')[0]
        contentUrl = json_data.get('contentUrl')
        relativeUrl = self.__getRelativePath(contentUrl)
        return self.doGet(relativeUrl)
	
    def __getWebContentUploadContent(self, courseId, webContentUploadId, contentPath):
        """Get content for a specific Web Content Upload in a course with
        ``GET /courses/{courseId}/webContentUpload/{webContentUploadId}`` and
        ``GET /courses/{courseId}/webContentUpload/{webContentUploadId}/content/{contentPath}``
        using OAuth2 as a student, teacher or teaching assistant.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param webContentUploadId: ID of the web content upload.
        :type webContentUploadId: str
        :param contentPath: Path of the content.
        :type contentPath: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_WEBCONTENTUPLOADS_CONTENT_ % (courseId, webContentUploadId, contentPath,)
        return self.doGet(relativeUrl)
        
    def getThreadedDiscussionResponseHierarchy(self, courseId, threadId, topicId, responseId):
        """Get hierarchy of a discussion thread response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/responseHierarchy``
        using OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEHIEARCHY % (courseId, threadId, topicId, responseId,)
        return self.doGet(relativeUrl)
        
    def getThreadedDiscussionUserViewResponses(self, userId, courseId, threadId, 
                                               topicId, responseId, depth = None):
        """Get all user's view statuses of a discussion thread response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/userviewresponses/{responseId}/userviewresponses``
        using OAuth2 as a student.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        :key depth: Number of levels to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if depth != None: return self.__getThreadedDiscussionUserViewResponses(userId, courseId, threadId,
                                                                               topicId, responseId, depth)
        
        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES_USERVIEWRESPONSES % (userId, courseId, 
                                                                                                           threadId, topicId, 
                                                                                                           responseId,)
        return self.doGet(relativeUrl)
        
    def __getThreadedDiscussionUserViewResponses(self, userId, courseId, threadId, topicId, 
                                                 responseId, depth):
        """Get all user's view statuses of a discussion thread response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/userviewresponses/{responseId}/userviewresponses?depth={depth}``
        using OAuth2 as a student.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        :param depth: Number of levels to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES_USERVIEWRESPONSES__DEPTH % (userId, courseId, 
                                                                                                                  threadId, topicId, 
                                                                                                                  responseId, depth,)
        return self.doGet(relativeUrl)

    def getThreadedDiscussionTopicUserViewResponses(self, userId, courseId, threadId, topicId, depth = None):
        """Get all user's view statuses of a discussion thread topic with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/userviewresponses``
        using OAuth2 as a student.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :key depth: Number of levels to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if depth != None: return self.__getThreadedDiscussionTopicUserViewResponses(userId, courseId, threadId, topicId, depth)

        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES % (userId, courseId, threadId, topicId,)
        return self.doGet(relativeUrl)
	
    def __getThreadedDiscussionTopicUserViewResponses(self, userId, courseId, threadId, topicId, depth):
        """Get all user's view statuses of a discussion thread topic with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/userviewresponses?depth={depth}``
        using OAuth2 as a student.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param depth: Number of levels to traverse
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_USERVIEWRESPONSES__DEPTH % (userId, courseId, threadId, topicId, depth,)
        return self.doGet(relativeUrl)
	
    def getThreadedDiscussionTopicHierarchy(self, courseId, threadId, topicId):
        """Get hierarchy of a discussion thread topic with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responseHierarchy``
        using OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSEHIEARCHY % (courseId, threadId, topicId,)
        return self.doGet(relativeUrl)
    
    def getThreadedDiscussionResponseCount(self, userId, courseId, threadId, topicId, responseId, depth = None):
        """Get count of responses for a specific response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/responseCounts``
        using OAuth1 or OAuth2 as a student.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        :key depth: Number of levels to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if depth != None: return self.__getThreadedDiscussionResponseCount(userId, courseId, threadId,
                                                                           topicId, responseId, depth)

        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSECOUNTS % (userId, courseId, 
                                                                                                threadId, topicId, 
                                                                                                responseId,)
        return self.doGet(relativeUrl)
	
    def __getThreadedDiscussionResponseCount(self, userId, courseId, threadId, topicId, responseId, depth):
        """Get count of responses for a specific response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/responseCounts?depth={depth}``
        using OAuth1 or OAuth2 as a student.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        :param depth: Number of levels to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSECOUNTS__DEPTH % (userId, courseId, 
                                                                                                       threadId, topicId, 
                                                                                                       responseId, depth)
        return self.doGet(relativeUrl)
	
    def getThreadedDiscussionTopicResponseCount(self, userId, courseId, threadId, topicId, depth = None):
        """Get count of responses for a specific topic with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responseCounts``
        using OAuth1 or OAuth2 as a student.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :key depth: Number of levels to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if depth != None: return self.__getThreadedDiscussionTopicResponseCount(userId, courseId, threadId, topicId, depth)
        
        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSECOUNTS % (userId, courseId, threadId, topicId,)
        return self.doGet(relativeUrl)
	
    def __getThreadedDiscussionTopicResponseCount(self, userId, courseId, threadId, topicId, depth):
        """Get count of responses for a specific topic with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responseCounts?depth={depth}``
        using OAuth1 or OAuth2 as a student.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param depth: Number of levels to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSECOUNTS__DEPTH % (userId, courseId, threadId, topicId, depth,)
        return self.doGet(relativeUrl)
	
    def getThreadedDiscussionResponseBranch(self, courseId, threadId, topicId, responseId):
        """Get branch hierarchy to a discussion thread response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/responseBranch``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response	
        :type responseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEBRANCH % (courseId, threadId, topicId, responseId,)
        return self.doGet(relativeUrl)
    
    def getThreadedDiscussionResponseAuthor(self, courseId, threadId, topicId, responseId):
        """Get author of a discussion thread response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/responseAuthor``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEAUTHOR % (courseId, threadId, topicId, responseId,)
        return self.doGet(relativeUrl)
    
    def getThreadedDiscussionResponseAndAuthorComposite(self, courseId, threadId, topicId, responseId, depth = None):
        """Get response and author composite of a discussion thread response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/responseAndAuthorComps``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        :key depth: Number of levels to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if depth != None: return self.__getThreadedDiscussionResponseAndAuthorComposite(courseId, threadId, topicId, responseId, depth)
        
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEANDAUTHORCOMPS % (courseId, threadId, topicId, responseId,)
        return self.doGet(relativeUrl)
    
    def __getThreadedDiscussionResponseAndAuthorComposite(self, courseId, threadId, topicId, responseId, depth):
        """Get response and author composite for a discussion thread response at a specified depth with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/responseAndAuthorComps?depth={depth}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        :param depth: Max depth to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSEANDAUTHORCOMPS__DEPTH % (courseId, threadId, 
                                                                                                         topicId, responseId, depth,)
        return self.doGet(relativeUrl)
    
    def getThreadedDiscussionTopicResponseAndAuthorComposite(self, courseId, threadId, topicId, depth = None):
        """Get response and author composite for a discussion thread topic with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responseAndAuthorComps/{responseId}/responseAndAuthorComps``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :key depth: Number of levels to traverse.
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if depth != None: return self.__getThreadedDiscussionTopicResponseAndAuthorComposite(courseId, threadId, topicId, depth)
        
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSEANDAUTHORCOMPS % (courseId, threadId, topicId,)
        return self.doGet(relativeUrl)
	
    def __getThreadedDiscussionTopicResponseAndAuthorComposite(self, courseId, threadId, topicId, depth):
        """Get response and author composite of a discussion thread topic at a specified depth with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responseAndAuthorComps/{responseId}/responseAndAuthorComps?depth={depth}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param depth: Max depth to traverse
        :type depth: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSEANDAUTHORCOMPS__DEPTH % (courseId, threadId, topicId, depth,)
        return self.doGet(relativeUrl)
	
    def getLastThreadedDiscussionResponse(self, userId, courseId):
        """Get a user's last threaded discussion response in a course with
        ``GET /users/{userId}/courses/{courseId}/threadeddiscussions/lastResponse``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS__LASTRESPONSE % (userId, courseId,)
        return self.doGet(relativeUrl)
	
    def getThreadedDiscussions(self, courseId, use_source_domain = None):
        """Get threaded dicussions for a course with
        ``GET /courses/{courseId}/threadeddiscussions``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :key use_source_domain: Indicator of whether to use the source domain in links.
        :type use_source_domain: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if use_source_domain == True: return self.__getThreadedDiscussions(courseId)

        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS % (courseId,)
        return self.doGet(relativeUrl)
	
    def __getThreadedDiscussions(self, courseId):
        """Get threaded dicussions for a course with
        ``GET /courses/{courseId}/threadeddiscussions?UseSourceDomain={useSourceDomain}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS__USESOURCEDOMAIN % (courseId,)
        return self.doGet(relativeUrl)
    
    def getThreadedDiscussionTopics(self, courseId, threadId, use_source_domain = None):
        """Get threaded dicussion topics for a course with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :key use_source_domain: Indicator of whether to use the source domain in links.
        :type use_source_domain: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if use_source_domain == True: return self.__getThreadedDiscussionTopics(courseId, threadId)
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS % (courseId, threadId,)
        return self.doGet(relativeUrl)
    
    def __getThreadedDiscussionTopics(self, courseId, threadId):
        """Get threaded dicussion topics for a course with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics?UseSourceDomain={useSourceDomain}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS__USESOURCEDOMAIN % (courseId, threadId,)
        return self.doGet(relativeUrl)
    
    def getThreadedDiscussionTopic(self, courseId, threadId, topicId, use_source_domain = None):
        """Get threaded dicussion topics for a course with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :key use_source_domain: Indicator of whether to use the source domain in links.
        :type use_source_domain: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.
        
        """
        if use_source_domain == True: return self.__getThreadedDiscussionTopic(courseId, threadId, topicId)
        
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_ %  (courseId, threadId, topicId,)
        return self.doGet(relativeUrl)
    
    def __getThreadedDiscussionTopic(self, courseId, threadId, topicId):
        """Get threaded dicussion topics for a course with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}?UseSourceDomain={useSourceDomain}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param useSourceDomain: Indicator of whether to use the source domain in links.
        :type useSourceDomain: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_USESOURCEDOMAIN % (courseId, threadId, topicId,)
        return self.doGet(relativeUrl)
	
    def getThreadedDiscussionResponseReadStatus(self, userId, courseId, threadId, topicId, responseId):
        """Get read status of a user's discussion thread response with
        ``GET /users/{userId}/courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/readStatus``
        using OAuth1 or OAuth2 as a student.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSE_READSTATUS % (userId, courseId, threadId, topicId, responseId,)
        return self.doGet(relativeUrl)
	
    def updateThreadedDiscussionResponseReadStatus(self, userId, courseId, threadId, 
                                                   topicId, responseId, readStatus):
        """Get read status of a user's discussion thread response with
        ``PUT /users/{userId}/courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/readStatus``
        using OAuth1 or OAuth2 as a student.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        :param readStatus: Read status Message.
        :type readStatus: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSE_READSTATUS % (userId, courseId, threadId, topicId, responseId,)
        return self.doPut(relativeUrl, body = readStatus)
	
    def getThreadedDiscussionResponses(self, courseId, threadId, topicId, responseId):
        """Get responses to a specific discussion thread response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/responses``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSES % (courseId, threadId, topicId, responseId,)
        return self.doGet(relativeUrl)
    
    def createThreadedDiscussionResponse(self, courseId, threadId, topicId, response_id = None, response_message = ""):
        """Create a response to a specific discussion thread response with
        ``POST /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}/responses``
        using OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :key response_id: ID of the response.
        :type response_id: str
        :key response_message: Response message to create.
        :type response_message: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        responseId = response_id
        responseMessage = response_message
        if responseId == None: return self.__createThreadedDiscussionResponse(courseId, threadId, topicId, responseMessage)
        
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_RESPONSES % (courseId, threadId, topicId, responseId,)
        return self.doPost(relativeUrl, body = responseMessage)
	
    def __createThreadedDiscussionResponse(self, courseId, threadId, topicId, responseMessage):
        """Create a response to a specific discussion thread topic with
        ``POST /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses``
        using OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseMessage: Response message to create.
        :type responseMessage: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES % (courseId, threadId, topicId,)
        return self.doPost(relativeUrl, body = responseMessage)
    
    def updateThreadedDiscussionResponse(self, courseId, threadId, topicId, responseId, responseMessage):
        """Update a response to a specific discussion thread response with
        ``PUT /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}``
        using OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseID: ID of the response.
        :type responseID: str
        :param responseMessage: Response message to create.
        :type responseMessage: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_ % (courseId, threadId, topicId, responseId,)
        return self.doPut(relativeUrl, body = responseMessage)
    
    def getThreadedDiscussionResponse(self, courseId, threadId, topicId, responseId):
        """Get a specific discussion thread response with
        ``GET /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}``
        using OAuth2 as a student, teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseId: ID of the response.
        :type responseId: str
        :param responseMessage: Response message to create.
        :type responseMessage: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_ % (courseId, threadId, topicId, responseId,)
        return self.doGet(relativeUrl)
    
    def deleteThreadedDiscussionResponse(self, courseId, threadId, topicId, responseId):
        """Delete a specific discussion thread response with
        ``DELETE /courses/{courseId}/threadeddiscussions/{threadId}/topics/{topicId}/responses/{responseId}``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or admin.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param threadId: ID of the thread.
        :type threadId: str
        :param topicId: ID of the topic.
        :type topicId: str
        :param responseID: ID of the response.
        :type responseID: str
        :param responseMessage: Response message to create.
        :type responseMessage: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_THREADEDDISCUSSIONS_TOPICS_RESPONSES_ % (courseId, threadId, topicId, responseId,)
        return self.doDelete(relativeUrl)

    def __getRelativePath(self, url):
        relativeUrl = None
		
        index = url.find(self.API_DOMAIN)
        if index > -1:
            index += len(self.API_DOMAIN)
            relativeUrl = url[index:]
        else :
            index = url.find(".com")
            if index > -1:
                index += 4
                relativeUrl = url[index:]
        return relativeUrl;
