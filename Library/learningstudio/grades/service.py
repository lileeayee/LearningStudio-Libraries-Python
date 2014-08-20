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

Defines a class that implements :class:`learningstudio.core.service.BasicService` for the Grades API.


"""

import json
from learningstudio.core.service import BasicService, HttpStatusCode
from learningstudio.oauth.util import json_loads

PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES = '/courses/%s/gradebook/customCategories'
PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_ = '/courses/%s/gradebook/customCategories/%s'
PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_CUSTOMITEMS = '/courses/%s/gradebook/customCategories/%s/customItems'
PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_CUSTOMITEMS_ = '/courses/%s/gradebook/customCategories/%s/customItems/%s'
PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_CUSTOMITEMS_GRADEBOOKITEM = '/courses/%s/gradebook/customCategories/%s/customItems/%s/gradebookItem'
PATH_COURSES_GRADEBOOKITEMS = '/courses/%s/gradebookItems'
PATH_COURSES_GRADEBOOKITEMS_ = '/courses/%s/gradebookItems/%s'
PATH_COURSES_GRADEBOOK__GRADEBOOKITEMS_ = '/courses/%s/gradebook/gradebookItems/%s'
PATH_COURSES_GRADEBOOKITEMS_GRADES = '/courses/%s/gradebookItems/%s/grades'
PATH_COURSES_GRADEBOOKITEMS_GRADES_ = '/courses/%s/gradebookItems/%s/grades/%s'
PATH_USERS_COURSES_GRADEBOOKITEMS_GRADE = '/users/%s/courses/%s/gradebookItems/%s/grade'
PATH_USERS_COURSES_USERGRADEBOOKITEMS = '/users/%s/courses/%s/userGradebookItems'
PATH_USERS_COURSES_USERGRADEBOOKITEMS__EXPANDGRADE = PATH_USERS_COURSES_USERGRADEBOOKITEMS+'?expand=grade'
PATH_USERS_COURSES_USERGRADEBOOKITEMS__USESOURCEDOMAIN = PATH_USERS_COURSES_USERGRADEBOOKITEMS+'?UseSourceDomain=true'
PATH_USERS_COURSES_USERGRADEBOOKITEMS__USESOURCEDOMAIN_EXPANDGRADE = PATH_USERS_COURSES_USERGRADEBOOKITEMS+'?UseSourceDomain=true&expand=grade'
PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS_GRADE = '/users/%s/courses/%s/gradebook/gradebookItems/%s/grade'
PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS_GRADE__USESOURCEDOMAIN = '/users/%s/courses/%s/gradebook/gradebookItems/%s/grade?UseSourceDomain=true'
PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS = '/users/%s/courses/%s/gradebook/userGradebookItems'
PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS__USESOURCEDOMAIN = '/users/%s/courses/%s/gradebook/userGradebookItems?UseSourceDomain=true'
PATH_USERS_COURSES_COURSEGRADETODATE = '/users/%s/courses/%s/coursegradetodate'
PATH_COURSES_GRADEBOOK__ROSTERCOURSEGRADESTODATE__STUDENTIDS_ = '/courses/%s/gradebook/rostercoursegradestodate?Student.ID=%s'
PATH_COURSES_GRADEBOOK__ROSTERCOURSEGRADESTODATE__OFFSET_LIMIT_ = '/courses/%s/gradebook/rostercoursegradestodate?offset=%s&limit=%s'
PATH_COURSES_GRADEBOOK__ROSTERCOURSEGRADESTODATE__STUDENTIDS_OFFSET_LIMIT_ = '/courses/%s/gradebook/rostercoursegradestodate?Student.ID=%s&offset=%s&limit=%s'
PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMS = '/users/%s/courses/%s/gradebook/userGradebookItems'
PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMS_ = '/users/%s/courses/%s/gradebook/userGradebookItems/%s'
PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMS_EXPANDGRADE = PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMS_+'?expand=grade'
PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMSTOTAL = '/users/%s/courses/%s/gradebook/userGradebookItemsTotals'

class GradeService(BasicService):
    """An implementation of BasicService for handling the Grades API.

    """

    def __init__(self, oauth_service_factory):
        super(GradeService, self).__init__(oauth_service_factory)
        
    def __getServiceIdentifier():
        return "LS-Library-Exam-Python-V1"

    def createCustomGradebookCategoryAndItem(self, courseId, customCategory, 
                                             customItem):
        """Create custom category and item with
        ``POST /courses/{courseId}/gradebook/customCategories``
        ``POST /courses/{courseId}/gradebook/customCategories/{customCategoryId}/customItems``
        using OAuth1 or OAuth2 as a teacher, teaching assistance or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategory: Custom category to create.
        :type customCategory: str
        :param customItem: Custom item to create.
        :type customItem: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        response = self.createCustomGradebookCategory(courseId, customCategory)
        if response.isError(): return response

        customCategoryObject = json_loads(response.getContent())
        customCategoryObject = customCategoryObject.get('customCategory')
        customCategoryId = customCategoryObject.get('guid')

        response = self.createCustomGradebookItem(courseId, customCategoryId, customItem)
        if response.isError(): return response
        
        customItemObject = json_loads(response.getContent())
        customItemObject = customItemObject.get('customItem')
        
        wrapper = {'customCategory' : customCategoryObject, 
                   'customItem' : customItemObject}
        response.setContent(json.dumps(wrapper))
        return response
    
    def createCustomGradebookCategory(self, courseId, customCategory):
        """Create custom gradebook category for a course with
        ``POST /courses/{courseId}/gradebook/customCategories``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategory: Custom category to create.
        :type customCategory: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES % (courseId,)
        return self.doPost(relativeUrl, body = customCategory)
    
    def updateCustomGradebookCategory(self, courseId, customCategoryId, 
                                      customCategory):
        """Create custom gradebook category for a course with
        ``PUT /courses/{courseId}/gradebook/customCategories/{customCategoryId}``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategoryId: ID of the custom category.
        :type customCategoryId: str
        :param customCategory: Custom category to create.
        :type customCategory: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_ % (courseId, customCategoryId,)
        return self.doPut(relativeUrl, body = customCategory)
    
    def deleteCustomGradebookCategory(self, courseId, customCategoryId):
        """Delete custom gradebook category for a course with
        ``DELETE /courses/{courseId}/gradebook/customCategories/{customCategoryId}``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategoryId: ID of the custom category.
        :type customCategoryId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_ % (courseId, customCategoryId,)
        return self.doDelete(relativeUrl)
    
    def getCustomGradebookCategory(self, courseId, customCategoryId):
        """Get custom gradebook category for a course with
        ``GET /courses/{courseId}/gradebook/customCategories/{customCategoryId}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategoryId: ID of the custom category.
        :type customCategoryId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_ % (courseId, customCategoryId,)
        return self.doGet(relativeUrl)
        
    def getCustomGradebookCategories(self, courseId):
        """Get custom gradebook categories for a course with
        ``GET /courses/{courseId}/gradebook/customCategories``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES % (courseId,)
        return self.doGet(relativeUrl)        
	
    def createCustomGradebookItem(self, courseId, customCategoryId, customItem):
        """Create custom gradebook item in a custom category for a course with
        ``POST /courses/{courseId}/gradebook/customCategories/{customCategoryId}/customItems``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategoryId: ID of the custom category.
        :type customCategoryId: str
        :param customItem: Custom item to create.
        :type customItem: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_CUSTOMITEMS % (courseId, customCategoryId,)
        return self.doPost(relativeUrl, body = customItem)
	
    def deleteCustomGradebookItem(self, courseId, customCategoryId, customItemId):
        """Delete custom gradebook item in a custom category for a course with
        ``DELETE /courses/{courseId}/gradebook/customCategories/{customCategoryId}/customItems/{customItemId}``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategoryId: ID of the custom category.
        :type customCategoryId: str
        :param customItemId: ID of the custom item.
        :type customItemId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_CUSTOMITEMS_ % (courseId, customCategoryId, customItemId,)
        return self.doDelete(relativeUrl)
    
    def getGradebookCustomItem(self, courseId, customCategoryId, customItemId):
        """Get custom item in a custom gradebook category for a course with
        ``GET /courses/{courseId}/gradebook/customCategories/{customCategoryId}/customItems/{customItemId}``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategoryId: ID of the custom category.
        :type customCategoryId: str
        :param customItemId: ID of the custom item.
        :type customItemId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_CUSTOMITEMS_ % (courseId, customCategoryId, customItemId,)
        return self.doGet(relativeUrl)
    
    def getCustomGradebookItem(self, courseId, customCategoryId, customItemId):
        """Get custom gradebook item in a custom category for a course with
        ``GET /courses/{courseId}/gradebook/customCategories/{customCategoryId}/customItems/{customItemId}``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategoryId: ID of the custom category.
        :type customCategoryId: str
        :param customItemId: ID of the custom item.
        :type customItemId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_CUSTOMITEMS_GRADEBOOKITEM % (courseId, customCategoryId, customItemId,)
        return self.doGet(relativeUrl)
        
    def getCustomGradebookItems(self, courseId, customCategoryId):
        """Get custom gradebook items in a custom category for a course with
        ``GET /courses/{courseId}/gradebook/customCategories/{customCategoryId}``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param customCategoryId: ID of the custom category.
        :type customCategoryId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__CUSTOMCATEGORIES_CUSTOMITEMS % (courseId, customCategoryId,)
        return self.doGet(relativeUrl)
	
    def getGradebookItems(self, courseId):
        """Get gradebook items for a course with
        ``GET /courses/{courseId}/gradebookItems``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOKITEMS % (courseId,)
        return self.doGet(relativeUrl)
    
    def getGradebookItem(self, courseId, gradebookItemId):
        """Get specific gradebook item for a course with
        ``GET /courses/{courseId}/gradebookItems/{gradebookItemId}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId:	ID of the gradebook item.
        :type gradebookItemId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOKITEMS_ % (courseId, gradebookItemId,)
        return self.doGet(relativeUrl)
    
    # Not Working!!!
    def createGradebookItem(self, courseId, gradebookItemId, gradebookItem):
        """Create specific gradebook item for a course with
        ``POST /courses/{courseId}/gradebook/gradebookItems/{gradebookItemId}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :param gradebookItem: Details of gradebook item.
        :type gradebookItem: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__GRADEBOOKITEMS_ % (courseId, gradebookItemId,)
        extraHeaders = {'X-METHOD-OVERRIDE' : 'PUT'}
        return self.doPost(relativeUrl, body = gradebookItem, extraHeaders = extraHeaders)
    
    def updateGradebookItem(self, courseId, gradebookItemId, gradebookItem):
        """Update specific gradebook item for a course with
        ``PUT /courses/{courseId}/gradebook/gradebookItems/{gradebookItemId}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :param gradebookItem: Details of gradebook item.
        :type gradebookItem: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__GRADEBOOKITEMS_ % (courseId, gradebookItemId,)
        return self.doPut(relativeUrl, body = gradebookItem)
    
    def getGradebookItemGrades(self, courseId, gradebookItemId,
                               graded_student_ids = None,
                               use_source_domain = None,
                               expand_user = None):
        """Get grades for specific gradebook item in a course with
        ``GET /courses/{courseId}/gradebookItems/{gradebookItemId}/grades``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :key graded_student_ids: IDs of graded students. (semicolon separated)
        :type graded_student_ids: str
        :key use_source_domain: Indicator of whether to include domains in urls.
        :type use_source_domain: bool
        :key expand_user: Indicator of whether to expand user info.
        :type expand_user: bool

        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if use_source_domain != None:
            return self.__getGradebookItemGrades(courseId, 
                                                 gradebookItemId,
                                                 graded_student_ids, 
                                                 use_source_domain,
                                                 expand_user)
        else:
            relativeUrl = PATH_COURSES_GRADEBOOKITEMS_GRADES % (courseId, gradebookItemId,)
            return self.doGet(relativeUrl)
	
    def __getGradebookItemGrades(self, courseId, gradebookItemId, 
                                 gradedStudentIds, useSourceDomain, 
                                 expandUser):
        """Get grades for specific gradebook item in a course using parameters with
        ``GET /courses/{courseId}/gradebookItems/{gradebookItemId}/grades?gradedStudents={gradedStudentIds}&useSourceDomains=true&expand=user``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId:	ID of the gradebook item.
        :type gradebookItemId: str
        :param gradedStudentIds: ID of students (semicolon separated).
        :type gradedStudentIds: str
        :param useSourceDomain: Indicator of whether to include domains in urls.
        :type useSourceDomain: str
        :param expandUser: Indicator of whether to expand user info 
        :type expandUser: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOKITEMS_GRADES % (courseId, gradebookItemId,)
        if gradedStudentIds != None or useSourceDomain or expandUser:
            relativeUrl += '?'
            firstParameter = True
            if gradedStudentIds != None:
                relativeUrl += 'gradedStudents=' + gradedStudentIds
                firstParameter = False
            if useSourceDomain:
                if not(firstParameter):
                    relativeUrl += '&'

                relativeUrl += 'UseSourceDomain=true'
                firstParameter = False

            if expandUser:
                if not(firstParameter):
                    relativeUrl += '&'

                relativeUrl += 'expand=user'
                firstParameter = False
		
        return self.doGet(relativeUrl)
	
    def getGradebookItemGrade(self, courseId, gradebookItemId, gradeId,
                              graded_student_ids = None, use_source_domain = None,
                              expand_user = None):
        """Get specific grade for an item in a course with
        ``GET /courses/{courseId}/gradebookItems/{gradebookItemId}/grades/{gradeId}``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :param gradeId: ID of the grade.
        :type gradeId: str
        :key graded_student_ids: ID of students (semicolon separated).
        :type graded_student_ids: str
        :key use_source_domain: Indicator of whether to include domains in urls
        :type use_source_domain: bool
        :key expand_user: Indicator of whether to expand user info.
        :type expand_user: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if use_source_domain != None:
            return self.__getGradebookItemGrade(courseId, 
                                                gradebookItemId, 
                                                gradeId,
                                                graded_student_ids, 
                                                use_source_domain,
                                                expand_user)
        else:
            relativeUrl = PATH_COURSES_GRADEBOOKITEMS_GRADES_ % (courseId, gradebookItemId, gradeId,)
            return self.doGet(relativeUrl)
	
    def __getGradebookItemGrade(self, courseId, gradebookItemId, gradeId, 
                                gradedStudentIds, useSourceDomain, expandUser):
        """Get specific grade for an item in a course using parameters with
        ``GET /courses/{courseId}/gradebookItems/{gradebookItemId}/grades/{gradeId}?gradedStudents={gradedStudentIds}&useSourceDomains=true&expand=user``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :param gradeId: ID of the grade within the gradebook.
        :type gradeId: str
        :param gradedStudentIds: ID of students (semicolon separated).
        :type gradedStudentIds: str
        :param useSourceDomain: Indicator of whether to include domains in urls.
        :type useSourceDomain: str
        :param expandUser: Indicator of whether to expand user info.
        :type expandUser: bool
	
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOKITEMS_GRADES_ % (courseId, gradebookItemId, gradeId,)
        if gradedStudentIds != None or useSourceDomain or expandUser:
            relativeUrl += '?'
            firstParameter = True
            if gradedStudentIds != None:
                relativeUrl += 'gradedStudents=' + gradedStudentIds
                firstParameter = False

            if useSourceDomain:
                if not(firstParameter):
                    relativeUrl += '&'

                relativeUrl += 'UseSourceDomain=true'
                firstParameter = False

            if expandUser:
                if not(firstParameter):
                    relativeUrl += '&'

                relativeUrl += 'expand=user'
                firstParameter = False
                    
        return self.doGet(relativeUrl)
	
    def createGradebookItemGrade(self, userId, courseId, gradebookItemId, grade):
        """Create user's grade for an item in a course with
        ``POST /users/{userId}/courses/{courseId}/gradebookItems/{gradebookItemId}/grade``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item
        :type gradebookItemId: str
        :param grade: Grade content to be created
        :type grade: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_GRADEBOOKITEMS_GRADE % (userId, courseId, gradebookItemId,)
        return self.doPost(relativeUrl, body = grade)
	
    def updateGradebookItemGrade(self, userId, courseId, gradebookItemId, grade):
        """Update user's grade for an item in a course with
        ``PUT /users/{userId}/courses/{courseId}/gradebookItems/{gradebookItemId}/grade``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :param grade: Grade content to be updated.
        :type grade: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_GRADEBOOKITEMS_GRADE % (userId, courseId, gradebookItemId,)
        return self.doPut(relativeUrl, body = grade)
	
    def deleteGradebookItemGrade(self, userId, courseId, gradebookItemId):
        """Delete user's grade for an item in a course with
        ``DELETE /users/{userId}/courses/{courseId}/gradebookItems/{gradebookItemId}/grade``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_GRADEBOOKITEMS_GRADE % (userId, courseId, gradebookItemId,)
        return self.doDelete(relativeUrl)

    def getUserGradebookItems(self, userId, courseId,
                              use_source_domain = None, expand_grade = None):
        """Get gradebook items for a user in a course with
        ``GET /users/{userId}/courses/{courseId}/userGradebookItems``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :key use_source_domain: Flag for using source domain parameter.
        :type use_source_domain: bool
        :key expand_grade: Flag for using expand domain parameter
        :type expand_grade: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if use_source_domain != None:
            return self.__getUserGradebookItems(userId, courseId, 
                                                use_source_domain, expand_grade)
        else:
            relativeUrl = PATH_USERS_COURSES_USERGRADEBOOKITEMS % (userId, courseId,)
            return self.doGet(relativeUrl)
		
    def __getUserGradebookItems(self, userId, courseId, useSourceDomain, expandGrade):
        """Get gradebook items for a user in a course with
        ``GET /users/{userId}/courses/{courseId}/userGradebookItems``
        with optional useSourceDomain and expand parameters
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param useSourceDomain: Flag for using source domain parameter.
        :type useSourceDomain: str
        :param expandDomain: Flag for using expand domain parameter.
        :type expandDomain: bool

        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        path = PATH_USERS_COURSES_USERGRADEBOOKITEMS
        if useSourceDomain or expandGrade:
            if useSourceDomain and expandGrade:
                path = PATH_USERS_COURSES_USERGRADEBOOKITEMS__USESOURCEDOMAIN_EXPANDGRADE
            elif useSourceDomain:
                path = PATH_USERS_COURSES_USERGRADEBOOKITEMS__USESOURCEDOMAIN
            else:
                path = PATH_USERS_COURSES_USERGRADEBOOKITEMS__EXPANDGRADE
		
        relativeUrl = path % (userId, courseId,)
        return self.doGet(relativeUrl)
	
    def createGrade(self, userId, courseId, gradebookItemId, grade):
        """Create a user's grade for an item in a course with
        ``POST /users/{userId}/courses/{courseId}/gradebook/gradebookItems/{gradebookItemId}/grade``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :param grade: Grade on the exam.
        :type grade: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS_GRADE % (userId, courseId, gradebookItemId,)
        return self.doPost(relativeUrl, body = grade)
	
    def updateGrade(self, userId, courseId, gradebookItemId, grade):
        """Update a user's grade for an item in a course with
        ``PUT /users/{userId}/courses/{courseId}/gradebook/gradebookItems/{gradebookItemId}/grade``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :param grade: Grade on the exam.
        :type grade: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS_GRADE % (userId, courseId, gradebookItemId,)
        return self.doPut(relativeUrl, body = grade)
	
    def deleteGrade(self, userId, courseId, gradebookItemId):
        """Delete a user's grade for an item in a course with
        ``DELETE /users/{userId}/courses/{courseId}/gradebook/gradebookItems/{gradebookItemId}/grade``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS_GRADE % (userId, courseId, gradebookItemId,)
        return self.doDelete(relativeUrl)
	
    def getGrade(self, userId, courseId, gradebookItemId, use_source_domain = None):
        """Get a user's grade for an item in a course with
        ``GET /users/{userId}/courses/{courseId}/gradebook/gradebookItems/{gradebookItemId}/grade``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :key use_source_domain: Flag for using source domain parameter.
        :type use_source_domain: bool

        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if use_source_domain != None:
            return self.__getGrade(userId, courseId, gradebookItemId, use_source_domain)
        else:
            relativeUrl = PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS_GRADE % (userId, courseId, gradebookItemId,)
            return self.doGet(relativeUrl)

    def __getGrade(self, userId, courseId, gradebookItemId, useSourceDomain):
        """Get a user's grade for an item in a course with override for useSourceDomain with
        ``GET /users/{userId}/courses/{courseId}/gradebook/gradebookItems/{gradebookItemId}/grade``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param gradebookItemId: ID of the gradebook item.
        :type gradebookItemId: str
        :param useSourceDomain: Indicator of whether to include domain in urls.
        :type useSourceDomain: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        path = PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS_GRADE__USESOURCEDOMAIN if useSourceDomain else PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS_GRADE
        relativeUrl = path % (userId, courseId, gradebookItemId,)
        return self.doGet(relativeUrl)
	
    def getGrades(self, userId, courseId, use_source_domain = None):
        """Get a user's grades for a course with
        ``GET /users/{userId}/courses/{courseId}/gradebook/userGradebookItems``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        Using OAuth2, student can also view their own grades (not create/update/delete).
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :key use_source_domain: Flag for using source domain parameter.
        :type use_source_domain: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if use_source_domain != None:
            return self.__getGrades(userId, courseId, use_source_domain)
        else:
            relativeUrl = PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS % (userId, courseId,)
            return self.doGet(relativeUrl)

    def __getGrades(self, userId, courseId, useSourceDomain):
        """Get a user's grades for a course with override for useSourceDomain with
        ``GET /users/{userId}/courses/{courseId}/gradebook/userGradebookItems``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param useSourceDomain: Indicator of whether to include domain in urls.
        :type useSourceDomain: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        path = PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS__USESOURCEDOMAIN if useSourceDomain else PATH_USERS_COURSES_GRADEBOOK__GRADEBOOKITEMS
        relativeUrl = path % (userId, courseId,)
        return self.doGet(relativeUrl)
        
	
    def getCurrentGrade(self, userId, courseId):
        """ Get a user's current grades for a course with
        ``GET /users/{userId}/courses/{courseId}/coursegradetodate``
        using OAuth1 or Auth2 as a student, teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_COURSEGRADETODATE % (userId, courseId,)
        return self.doGet(relativeUrl)
	
    def getCurrentGrades(self, courseId, student_ids = None, offset = None, limit = None):
        """Get current grades for all students in a course with
        ``GET /courses/{courseId}/gradebook/rostercoursegradestodate?offset={offset}&limit={limit}``
        using OAuth1 or Auth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of course.
        :type courseId: str
        :key offset: Offset position
        :type offset: int
        :key limit: Limitation on count of records.
        :type limit: int
        :key student_ids: Comma-separated list of students to filter.
        :type student_ids: str
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if offset == None:
            return self.__getCurrentGradesWithoutOffset(courseId, student_ids)
        elif student_ids != None:
            return self.__getCurrentGrades(courseId, student_ids, offset, limit)
        else:
            relativeUrl = PATH_COURSES_GRADEBOOK__ROSTERCOURSEGRADESTODATE__OFFSET_LIMIT_ % (courseId, str(offset), str(limit),)
            return self.doGet(relativeUrl)
	
    def __getCurrentGrades(self, courseId, studentIds, offset, limit):
        """Get current grades for specific students in a course with
        ``GET /courses/{courseId}/gradebook/rostercoursegradestodate?Student.ID={studentIds}&offset={offset}&limit={limit}``
        using OAuth1 or Auth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of course.
        :type courseId: str
        :param studentIds: Comma-separated list of students to filter.
        :type studentIds: str
        :param offset: Offset position.
        :type offset: int
        :param limit: Limitation on count of records.
        :type limit: int
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__ROSTERCOURSEGRADESTODATE__STUDENTIDS_OFFSET_LIMIT_ % (courseId, studentIds, 
                                                                                                    str(offset), str(limit),)
        return  self.doGet(relativeUrl)
	
    def __getCurrentGradesWithoutOffset(self, courseId, studentIds):
        """Get current grades for specific students in a course with
        ``GET /courses/{courseId}/gradebook/rostercoursegradestodate?Student.ID={studentIds}``
        using OAuth1 or Auth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of course.
        :type courseId: str
        :param studentIds: Comma-separated list of students to filter.
        :type studentIds: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_GRADEBOOK__ROSTERCOURSEGRADESTODATE__STUDENTIDS_ % (courseId, studentIds,)
        return self.doGet(relativeUrl)
	
    def getCourseGradebookUserItems(self, userId, courseId):
        """Get user gradebook items in a course gradebook with
        ``GET /users/{userId}/courses/{courseId}/gradebook/userGradebookItems``
        using OAuth1 or Auth2 as a student, teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMS % (userId, courseId,)
        return self.doGet(relativeUrl)
	
    def getCourseGradebookUserItem(self, userId, courseId, userGradebookItemId, expand_grade = None):
        """Get user gradebook item in a course gradebook by user gradebook item id with
        ``GET /users/{userId}/courses/{courseId}/gradebook/userGradebookItems/{userGradebookItemId}``
        using OAuth1 or Auth2 as a student, teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param userGradebookItemId: concatenation of {userId}-{gradebookItemGuid}.
        :type userGradebookItemId: str
        :key expand_grade: Flag of whether to expand grade data.
        :type expand_grade: bool
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        if expand_grade != None:
            return self.__getCourseGradebookUserItem(userId, courseId, userGradebookItemId, expand_grade)
        else:
            relativeUrl = PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMS_ % (userId, courseId, userGradebookItemId,)
            return self.doGet(relativeUrl)
	
    def __getCourseGradebookUserItem(self, userId, courseId, userGradebookItemId, expandGrade):
        """ Get user gradebook item in a course gradebook by user gradebook item id with
        ``GET /users/{userId}/courses/{courseId}/gradebook/userGradebookItems/{userGradebookItem}``
        or ``GET /users/{userId}/courses/{courseId}/gradebook/userGradebookItems/{userGradebookItem}?expandGrade=true``
        using OAuth1 or Auth2 as a student, teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param userGradebookItemId: concatenation of {userId}-{gradebookItemGuid}.
        :type userGradebookItemId: str
        :param expandGrade: Flag of whether to expand grade data.
        :type expandGrade: bool
            
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        path = PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMS_EXPANDGRADE if expandGrade else PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMS_
        relativeUrl = path % (userId, courseId, userGradebookItemId,)
        return self.doGet(relativeUrl)
	
    def getTotalPointsAvailable(self, userId, courseId):
        """Get summary of points available to a student in a course with
        ``GET /users/{userId}/courses/{courseId}/gradebook/userGradebookItemsTotals``
        using OAuth1 or Auth2 as a student, teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_USERS_COURSES_GRADEBOOK__USERGRADEBOOKITEMSTOTAL % (userId, courseId,)
        return self.doGet(relativeUrl)

