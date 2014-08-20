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

Defines a class that implements :class:`learningstudio.core.service.BasicService` for the Exams API.


"""

import json
from learningstudio.core.service import BasicService, HttpStatusCode
from learningstudio.oauth.util import json_loads

# Relation Constants.
RELS_USER_COURSE_EXAM = 'https://api.learningstudio.com/rels/user/course/exam'
	
# Path Constants.
PATH_USERS_COURSES_ITEMS = '/users/%s/courses/%s/items'
PATH_USERS_COURSES_EXAMS = '/users/%s/courses/%s/exams'
PATH_USERS_COURSES_EXAMS_ = '/users/%s/courses/%s/exams/%s'
PATH_USERS_COURSES_EXAMS_ATTEMPTS = '/users/%s/courses/%s/exams/%s/attempts'
PATH_USERS_COURSES_EXAMS_ATTEMPTS_ = '/users/%s/courses/%s/exams/%s/attempts/%s'
PATH_USERS_COURSES_EXAMS_ATTEMPTS_SUMMARY = '/users/%s/courses/%s/exams/%s/attempts/%s/summary'
PATH_USERS_COURSES_EXAMDETAILS = '/users/%s/courses/%s/examDetails'
PATH_USERS_COURSES_EXAMDETAILS_ = '/users/%s/courses/%s/examDetails/%s'
PATH_COURSES_EXAMSCHEDULES = '/courses/%s/examSchedules'

PATH_USERS_COURSES_EXAMS_SECTIONS = '/users/%s/courses/%s/exams/%s/sections'
PATH_USERS_COURSES_EXAMS_SECTIONS_QUESTIONS = '/users/%s/courses/%s/exams/%s/sections/%s/questions'

PATH_USERS_COURSES_EXAMS_SECTIONS_TRUEFALSE_ = '/users/%s/courses/%s/exams/%s/sections/%s/trueFalseQuestions/%s'
PATH_USERS_COURSES_EXAMS_SECTIONS_TRUEFALSE_CHOICES = '/users/%s/courses/%s/exams/%s/sections/%s/trueFalseQuestions/%s/choices'

PATH_USERS_COURSES_EXAMS_SECTIONS_MULTIPLECHOICE_ = '/users/%s/courses/%s/exams/%s/sections/%s/multipleChoiceQuestions/%s'
PATH_USERS_COURSES_EXAMS_SECTIONS_MULTIPLECHOICE_CHOICES = '/users/%s/courses/%s/exams/%s/sections/%s/multipleChoiceQuestions/%s/choices'

PATH_USERS_COURSES_EXAMS_SECTIONS_MANYMULTIPLECHOICE_ = '/users/%s/courses/%s/exams/%s/sections/%s/manyMultipleChoiceQuestions/%s'
PATH_USERS_COURSES_EXAMS_SECTIONS_MANYMULTIPLECHOICE_CHOICES = '/users/%s/courses/%s/exams/%s/sections/%s/manyMultipleChoiceQuestions/%s/choices'

PATH_USERS_COURSES_EXAMS_SECTIONS_MATCHING_ = '/users/%s/courses/%s/exams/%s/sections/%s/matchingQuestions/%s'
PATH_USERS_COURSES_EXAMS_SECTIONS_MATCHING_PREMISES = '/users/%s/courses/%s/exams/%s/sections/%s/matchingQuestions/%s/premises'
PATH_USERS_COURSES_EXAMS_SECTIONS_MATCHING_CHOICES = '/users/%s/courses/%s/exams/%s/sections/%s/matchingQuestions/%s/choices'

PATH_USERS_COURSES_EXAMS_SECTIONS_SHORT_ = '/users/%s/courses/%s/exams/%s/sections/%s/shortQuestions/%s'
PATH_USERS_COURSES_EXAMS_SECTIONS_ESSAY_ = '/users/%s/courses/%s/exams/%s/sections/%s/essayQuestions/%s'
PATH_USERS_COURSES_EXAMS_SECTIONS_FILLINTHEBLANK_ = '/users/%s/courses/%s/exams/%s/sections/%s/fillintheblankQuestions/%s'

PATH_USERS_COURSES_EXAMS_ATTEMPTS_ANSWERS = '/users/%s/courses/%s/exams/%s/attempts/%s/answers'
PATH_USERS_COURSES_EXAMS_ATTEMPTS_ANSWERS_ = '/users/%s/courses/%s/exams/%s/attempts/%s/answers/%s'

# Exam Constants.
PEARSON_EXAM_TOKEN = 'Pearson-Exam-Token'
PEARSON_EXAM_PASSWORD = 'Pearson-Exam-Password'

class QuestionType:
    TRUE_FALSE = 'trueFalse'
    MULTIPLE_CHOICE = 'multipleChoice'
    MANY_MULTIPLE_CHOICE = 'manyMultipleChoice'
    MATCHING = 'matching'
    SHORT_ANSWER = 'short'
    ESSAY = 'essay'
    FILL_IN_THE_BLANK = 'fillInTheBlank'
    
    VALUES = [TRUE_FALSE, MULTIPLE_CHOICE, 
              MANY_MULTIPLE_CHOICE, MATCHING, 
              SHORT_ANSWER, ESSAY, 
              FILL_IN_THE_BLANK]

    @staticmethod
    def matchesValue(v):
        v = v.lower()
        for qt in QuestionType.VALUES:
            if qt.lower() == v:
                return qt
        return None

class ExamService(BasicService):
    """An implementation of BasicService for handling the Exams API.

    """

    def __init__(self, oauth_service_factory):
        super(ExamService, self).__init__(oauth_service_factory)

    def __getServiceIdentifier():
        return "LS-Library-Exam-Python-V1"
    
    def getAllExamItems(self, user_id, course_id):
        """Retrieve all of a user's exams for a course with ``GET /users/{userId}/courses/{courses}/items``
        using OAuth1 or OAuth2 as a student or teacher.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: - ID of course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relative_url = PATH_USERS_COURSES_ITEMS % (user_id, course_id)
        response = self.doGet(relative_url)
        if response.isError(): return response
        course_items_json = response.getContent()
        json_obj = json_loads(course_items_json)
        items = json_obj.get('items', [])
        exams = []
        for item in items:
            links = item.get('links', [])
            for link in links:
                if RELS_USER_COURSE_EXAM == link.get('rel', ''): 
                    exams.append(item)
                    break
            
        exam_items = {'items' : exams}
        response.setContent(json.dumps(exam_items))
        return response

    def getExamDetails(self, userId, courseId, exam_id = None):
        """Retrieve details for all exams for a course with ``GET /users/{userId}/courses/{courseId}/exams``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :key exam_id: ID of the exam.
        :type exam_id: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = (PATH_USERS_COURSES_EXAMDETAILS % (userId, courseId,)) if exam_id == None else (PATH_USERS_COURSES_EXAMDETAILS_ % (userId,
                                                                                                                                         courseId,
                                                                                                                                         exam_id,))
        return self.doGet(relativeUrl)
	
    def getExamSchedules(self, courseId):
        """Retrieve exam schedules for a course with ``GET /courses/{courseId}/examschedules``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.
        
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relativeUrl = PATH_COURSES_EXAMSCHEDULES % (courseId,)
        return self.doGet(relativeUrl)

    def getExistingExams(self, user_id, course_id):
        """Retrieve all of a user's existing exams for a course with ``GET /users/{userId}/courses/{courseId}/exams`` 
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        return self.doGet(PATH_USERS_COURSES_EXAMS % (user_id, course_id,))

    def getExistingExam(self, user_id, course_id, exam_id):
        """Retrieve a user's exam for a course with ``GET /users/{userId}/courses/{courseId}/exams/{examId}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        return self.doGet(PATH_USERS_COURSES_EXAMS_ % (user_id, course_id, exam_id,))

    def createUserExam(self, user_id, course_id, exam_id):
        """Creates an exam for a user in a course with ``POST /users/userId/courses/{courseId}/exams/{examId}``
        using OAuth2 as a student.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        response = self.getExistingExam(user_id, course_id, exam_id)
        if response.getStatusCode() == HttpStatusCode.NOT_FOUND:
            return self.doPost(PATH_USERS_COURSES_EXAMS_ % (user_id, course_id, exam_id,))
        return response

    def deleteUserExam(self, user_id, course_id, exam_id):
        """Delete a users's exam in a course with ``DELETE /users/{userId}/courses/{courseId}/exams/{examId}``
        using OAuth1 or OAuth2 as a teacher, teaching assistant or administrator.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        return self.doDelete(PATH_USERS_COURSES_EXAMS_ % (user_id, course_id, exam_id,))
    
    def createExamAttempt(self, user_id, course_id, exam_id, exam_password = None):
        """Create an exam attempt for a user in a course with ``POST /users/{userId}/courses/{courseId}/exams/{examId}/attempts``
        using OAuth1 or OAuth2 as student, teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        :key exam_password: Optional password from instructor.
        :type exam_password: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        exam_headers = None
        if exam_password != None: exam_headers = {PEARSON_EXAM_PASSWORD : exam_password}
        return self.doPost(PATH_USERS_COURSES_EXAMS_ATTEMPTS % (user_id, course_id, exam_id,),
                                     extra_headers = exam_headers)                                     
                                     
    def getExamAttempts(self, user_id, course_id, exam_id):
        """Retrieve a users's attempt of an exam in a course with ``GET /users/{userId}/courses/{courseId}/exams/{examId}/attempts``
        using OAuth2 as a student.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        return self.doGet(PATH_USERS_COURSES_EXAMS_ATTEMPTS % (user_id, course_id, exam_id,))

    def getExamAttempt(self, user_id, course_id, exam_id, attempt_id):
        """Retrieve a user's attempt of an exam in a course with ``GET /users/{userId}/courses/{courseId}/exams/{examId}/attempts/{attemptId}``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        :param attemptId: ID of the exam attempt.
        :type attemptId: str

        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        return self.doGet(PATH_USERS_COURSES_EXAMS_ATTEMPTS_ % (user_id, course_id, exam_id, attempt_id,))
    
    def getCurrentExamAttempt(self, user_id, course_id, exam_id):
        """Retrieves and filters a user's current attempt of an exam in a course with 
        ``GET /users/{userId}/courses/{courseId}/exams/{examId}/attempts`` using OAuth2 as a student.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        response = self.getExamAttempts(user_id, course_id, exam_id)
        if response.isError(): return response
        attempts_json = response.getContent()
        json_obj = json_loads(attempts_json)
        attempts = json_obj.get('attempts', [])
        current_attempt = None
		
        for attempt in attempts:
            if not(bool(attempt.get('isCompleted', False))):
                current_attempt = attempt
                break
		
        if current_attempt != None:
            attempt = {'attempt' : current_attempt}
            response.setContent(json.dumps(attempt))
        else:
            response.setStatusCode(HttpStatusCode.NOT_FOUND)
            response.setContent('')
        return response;

    def getExamAttemptSummary(self, user_id, course_id, exam_id, attempt_id):
        """Retrieve a summary of a user's attempt of an exam in a course with 
        ``GET /users/{userId}/courses/{courseId}/exams/{examId}/attempts/{attempdId}/summary`` using OAuth2 as a student.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param attemptId: ID of the attempt.
        :type attemptId: str

        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        return self.doGet(PATH_USERS_COURSES_EXAMS_ATTEMPTS_SUMMARY % (user_id, course_id,
                                                                         exam_id, attempt_id,))

    def startExamAttempt(self, user_id, course_id, exam_id, exam_password = None):
        """Retrieve a user's current attempt or create new attempt of an exam in a course with
        getCurrentExamAttempt and createExamAttempt using OAuth2 as a student.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        :key exam_password: Optional password from instructor.
        :type exam_password: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        response = self.getCurrentExamAttempt(user_id, course_id, exam_id)
        if response.getStatusCode() == HttpStatusCode.NOT_FOUND:
            response = self.createExamAttempt(user_id, course_id, exam_id, exam_password)
        return response

    def getExamSections(self, user_id, course_id, exam_id):
        """Retrieve sections of an user's exam in a course with ``GET /users/{userId}/courses/{courseId}/exams/{examId}/sections``
        using OAuth1 or OAuth2 as a student, teacher, teaching assistant or administrator.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str

        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        return self.doGet(PATH_USERS_COURSES_EXAMS_SECTIONS % (user_id, course_id, exam_id,))

    def getExamSectionQuestions(self, user_id, course_id, exam_id, section_id):
        """Retrieve details of questions for a section of a user's exam in a course with 
        ``GET /users/{userId}/courses/{courseId}/exams/{examId}/sections/{sectionId}/questions``
        and getExamSectionQuestion using OAuth2 as a student.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        :param sectionId: ID of the section on the exam.
        :type sectionId: str
        
	:returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_QUESTIONS % (user_id, course_id, exam_id, section_id,)
        response = self.doGet(relative_url)
        if response.isError(): return response
        json_obj = json_loads(response.getContent())
        questions = json_obj.get('questions', [])
        section_questions = []
		
        for question in questions:
            question_type = question.get('type', '')
            question_id = question.get('id', '')
            question_response = self.getExamSectionQuestion(user_id, course_id,
                                                            exam_id, section_id,
                                                            question_type, question_id)
            if question_response.isError(): return question_response
            section_question = json_loads(question_response.getContent())
            section_question['type'] = question_type
            section_question['id'] = question_id
            section_question['pointsPossible'] = question.get('pointsPossible')
            section_questions.append(section_question)
		
        response.setContent(json.dumps({'questions' : section_questions}))
        return response

    def getQuestionAnswer(self, userId, courseId, examId, 
                          attemptId, questionId):
        """Retrieve a user's answer for a question on a specific attempt of an exam in a course with
        ``GET /users/{userId}/courses/{courseId}/exams/{examId}/attempts/{attemptId}/answers/{answerId}``
        using OAuth2 as a student.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        :param attemptId: ID of the attempt on the exam.
        :type attemptId: str
        :param questionId: ID of the question on the exam.
        :type questionId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        response = self.getExamAttempt(userId, courseId, examId, attemptId)
        if response.isError(): return response
        extraHeaders = self.__get_exam_headers(response)
		
        relativeUrl = PATH_USERS_COURSES_EXAMS_ATTEMPTS_ANSWERS_ % (userId, courseId, examId, attemptId, questionId,)
        return self.doGet(relativeUrl, extra_headers = extraHeaders)

    def __get_section_urls(self, user_id, course_id, exam_id, section_id,
                           question_id, qtype):
        question_relative_url = None
        choices_relative_url = None
        premises_relative_url = None
		
        if qtype == QuestionType.TRUE_FALSE:
            question_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_TRUEFALSE_ % (user_id, course_id, 
                                                                                    exam_id, section_id, 
                                                                                    question_id,)
            choices_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_TRUEFALSE_CHOICES % (user_id, course_id, 
                                                                                          exam_id, section_id, 
                                                                                          question_id,)
        elif qtype == QuestionType.MULTIPLE_CHOICE:
            question_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_MULTIPLECHOICE_ % (user_id, course_id, 
                                                                                         exam_id, section_id, 
                                                                                         question_id,)
            choices_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_MULTIPLECHOICE_CHOICES % (user_id, course_id, 
                                                                                               exam_id, section_id, 
                                                                                               question_id,)
        elif qtype == QuestionType.MANY_MULTIPLE_CHOICE:
            question_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_MANYMULTIPLECHOICE_ % (user_id, course_id, 
                                                                                             exam_id, section_id, 
                                                                                             question_id,)
            choices_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_MANYMULTIPLECHOICE_CHOICES % (user_id, course_id, 
                                                                                                   exam_id, section_id, 
                                                                                                   question_id,)
        elif qtype == QuestionType.MATCHING:
            question_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_MATCHING_ % (user_id, course_id, 
                                                                                   exam_id, section_id, 
                                                                                   question_id,)
            premises_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_MATCHING_PREMISES % (user_id, course_id, 
                                                                                           exam_id, section_id, 
                                                                                           question_id,)
            choices_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_MATCHING_CHOICES % (user_id, course_id, 
                                                                                         exam_id, section_id, 
                                                                                         question_id,)
        elif qtype == QuestionType.SHORT_ANSWER:
            question_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_SHORT_ % (user_id, course_id, 
                                                                                exam_id, section_id, 
                                                                                question_id,)
        elif qtype == QuestionType.ESSAY:
            question_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_ESSAY_  % (user_id, course_id, 
                                                                                 exam_id, section_id, 
                                                                                 question_id,)
        elif qtype == QuestionType.FILL_IN_THE_BLANK:
            question_relative_url = PATH_USERS_COURSES_EXAMS_SECTIONS_FILLINTHEBLANK_ % (user_id, course_id, 
                                                                                         exam_id, section_id, 
                                                                                         question_id,)
        return (question_relative_url, choices_relative_url, premises_relative_url)
        
    def getExamSectionQuestion(self, user_id, course_id, exam_id, section_id, 
                               question_type, question_id):
        """Retrieve details of a question for a section of a user's exam in a course with 
        ``GET /users/{userId}/courses/{courseId}/exams/{examId}/sections/{sectionId}/{questionType}Questions/{questionId}``, 
        ``GET /users/{userId}/courses/{courseId}/exams/{examId}/sections/{sectionId}/{questionType}Questions/{questionId}/choices`` and 
        ``GET /users/{userId}/courses/{courseId}/exams/{examId}/sections/{sectionId}/{questionType}Questions/{questionId}/premises`` 
        using OAuth2 as a student.
        
        :param userId: ID of the user.
        :type userId: str
        :param examId: ID of the exam.
        :type examId: str
        :param sectionId: ID of the section.
        :type sectionId: str
        :param questionType: Type of question.
        :type questionType: str
        :param questionId: ID of the question.
        :type questionId: str

        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        qtype = QuestionType.matchesValue(question_type)
        if qtype == None: raise RuntimeError('Invalid Question Type.')

        response = self.getCurrentExamAttempt(user_id, course_id, exam_id)
        if response.isError(): return response

        extra_headers = self.__get_exam_headers(response)
		
        question_relative_url, choices_relative_url, premises_relative_url = self.__get_section_urls(user_id, course_id,
                                                                                                     exam_id, section_id,
                                                                                                     question_id, qtype)
		
        response = self.doGet(question_relative_url, extra_headers = extra_headers)
        if response.isError(): return response
		
        question = json_loads(response.getContent())
        details = {'question' : question.get(qtype + 'Question')}
		
        if choices_relative_url != None:
            response = self.doGet(choices_relative_url, extra_headers = extra_headers)
            if response.isError(): return response
            choices = json_loads(response.getContent())
            details['choices'] = choices.get('choices', [])
		
        if premises_relative_url != None:
            response = self.doGet(premises_relative_url, extra_headers = extra_headers)
            if response.isError(): return response
            premises = json_loads(response.getContent())
            details['premises'] = premises.get('premises', [])
            
        response.setContent(json.dumps(details))
        return response
                                    
    def answerQuestion(self, user_id, course_id, 
                       exam_id, attempt_id, 
                       question_id, answer):
        """Updates a user's answer for a question on a specific attempt of an exam in a course with
        ``GET /users/{userId}/courses/{courseId}/exams/{examId}/attempts/{attemptId}/answers/{answerId}``,
        ``POST /users/{userId}/courses/{courseId}/exams/{examId}/attempts/{attemptId}/answers`` and 
        ``PUT /users/{userId}/courses/{courseId}/exams/{examId}/attempts/{attemptId}/answers/{answerId}``
        using OAuth2 as a student.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        :param attemptId: ID of the attempt on the exam.
        :type attemptId: str
        :param questionId: ID of the question on the exam.
        :type questionId: str
        :param answer: Answer to the question on the exam.
        :type answer: str

        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        response = self.getCurrentExamAttempt(user_id, course_id, exam_id)
        if response.isError(): return response

        extra_headers = self.__get_exam_headers(response)
		
        relative_url = PATH_USERS_COURSES_EXAMS_ATTEMPTS_ANSWERS_ % (user_id, course_id, 
                                                                     exam_id, attempt_id, 
                                                                     question_id,)
        response = self.doGet(relative_url, extra_headers = extra_headers)
        if response.isError():
            if response.getStatusCode() == HttpStatusCode.NOT_FOUND:
                response = self.doPost(PATH_USERS_COURSES_EXAMS_ATTEMPTS_ANSWERS % (user_id, course_id, 
                                                                                    exam_id, attempt_id,),
                                                 extra_headers = extra_headers, 
                                                 body = answer)
        else:
            response = self.doPut(relative_url, extra_headers = extra_headers, body = answer)
            
        return response

    def completeExamAttempt(self, user_id, course_id, exam_id, attempt_id):
        """Updates a user's attempt of an exam in a course to complete with 
        ``PUT /users/{userId}/courses/{examId}/exams/{examId}/attempts/{attemptId}`` using OAuth2 as student.

        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        :param attemptId: ID of the attempt on the exam.
        :type attemptId: str

        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """
        response = self.getCurrentExamAttempt(user_id, course_id, exam_id)
        if response.isError(): return response
        extra_headers = self.__get_exam_headers(response)
        return self.doPut(PATH_USERS_COURSES_EXAMS_ATTEMPTS_ % (user_id, course_id,
                                                                exam_id, attempt_id,),
                                    extra_headers = extra_headers,  
                                    body = '{ "attempts" : { "isCompleted" : true } }')

    def deleteQuestionAnswer(self, userId, courseId, examId, 
                             attemptId, questionId):
        """Delete a user's answer for a question on a specific attempt of an exam in a course with
        ``DELETE /users/{userId}/courses/{courseId}/exams/{examId}/attempts/{attemptId}/answers/{answerId}``
        using OAuth2 as a student.
        
        :param userId: ID of the user.
        :type userId: str
        :param courseId: ID of the course.
        :type courseId: str
        :param examId: ID of the exam.
        :type examId: str
        :param attemptId: ID of the attempt on the exam.
        :type attemptId: str
        :param questionId: ID of the question on the exam.
        :type questionId: str
        
        :returns: A :class:`learningstudio.core.Response` object with details of status and content.

        """

        response = self.getExamAttempt(userId,courseId,examId,attemptId)
        if response.isError(): return response
        extraHeaders = self.__get_exam_headers(response)
        
        relativeUrl = PATH_USERS_COURSES_EXAMS_ATTEMPTS_ANSWERS_ % (userId, courseId, examId, attemptId, questionId,)
        return self.doDelete(relativeUrl, extra_headers = extraHeaders)


    def __get_exam_headers(self, response):
        attempt = json_loads(response.getContent())
        attempt = attempt.get('attempt')
        return {PEARSON_EXAM_TOKEN : attempt.get('pearsonExamToken', '')}
