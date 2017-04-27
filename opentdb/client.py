from .categories import categories
from .exceptions import (ConnectionError, HTTPError, APIError)
from .question import Question
import requests
from HTMLParser import HTMLParser

class Client(object):
    def __init__(self):
        self.__API_BASEURL = 'https://opentdb.com'
        self.__API_ENDPOINT = '/api.php'
        self.__API_TOKEN_ENDPOINT = '/api_token.php'
        self.__API_TOKEN = False

    def __apiRequest(self, url, params):
        """
            Used internally by the Client object to make calls to the API.
            Parameters:
                -url: the URL of the API endpoint.
                -params: parameters for the request.
            Returns the JSON response in the form of a Dictionary.
            Otherwise, an exception is raised.
        """
        try:
            response = requests.get(url, params=params)
        except requests.exceptions.RequestException:
            raise ConnectionError('Failed to connect to OpenTDB.')
        try:
            response.raise_for_status()
            response = response.json()
            assert response['response_code'] == 0
            return response
        except requests.exceptions.HTTPError:
            raise HTTPError('The request to OpenTDB returned an error.')
        except ValueError:
            raise APIError('OpenTDB returned an invalid JSON response.')
        except AssertionError:
            raise APIError('OpenTDB refused session token request.')
        except:
            raise OpenTDBException('An unknown error occurred while parsing the response.')


    def getToken(self):
        """
            Requests a session token from the API.
            Returns True if session token was successfully obtained.
            Otherwise, an exception is raised.
        """
        url = self.__API_BASEURL + self.__API_TOKEN_ENDPOINT
        params = { 'command': 'request' }
        response = self.__apiRequest(url, params)
        self.__API_TOKEN = response['token']
        return True

    def printToken(self):
        return self.__API_TOKEN

    def getQuestions(self, amount=10, category=0, use_token=False):
        """
            Requests a set of questions from the API.
            Parameters:
                -amount:    how many questions to request.
                -category:  which category the questions should be from.
                            If this is set to False, questions will be from all categories.
                -use_session_token: whether or not to use the token,
                                    which is generated with getToken()
            Returns a List of Question objects.
        """
        url = self.__API_BASEURL + self.__API_ENDPOINT
        params = { 'amount': amount }
        try:
            params['category'] = int(category)
        except:
            params['category'] = 0
        if use_token and self.__API_TOKEN:
            params['token'] = self.__API_TOKEN
        response = self.__apiRequest(url, params)
        questions_from_tdb = response['results']
        unescape = HTMLParser().unescape
        questions_list = []
        for question_dict in questions_from_tdb:
            category = unescape(question_dict['category'])
            type = question_dict['type']
            difficulty = question_dict['difficulty']
            question = unescape(question_dict['question'])
            correct_answer = unescape(question_dict['correct_answer'])
            incorrect_answers = unescape(question_dict['incorrect_answers'])
            questions_list.append(Question(category=category, type=type, difficulty=difficulty, question=question, correct_answer=correct_answer, incorrect_answers=incorrect_answers))
        return questions_list

    def getCategories(self):
        """
            Returns a Dictionary in the form:
                categories['Category Name'] = category_id.
                (category_id is an integer)
        """
        return categories
