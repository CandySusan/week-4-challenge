from __future__ import print_function, unicode_literals

import json
import os
from pprint import pprint

import requests
from PyInquirer import Separator, Token, prompt, style_from_dict
from requests.auth import HTTPDigestAuth

style = style_from_dict(
    {
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    }
)


class NewsApi():

    def get_api_key(self):
        return os.getenv("NEWS_API_KEY")

    def get_news_channel(self, api_key):
        if not api_key:
            raise ValueError("Your APi key is missing")

        questions = [
            {
                'type': 'list',
                'message': 'Select news source',
                'name': 'source',
                'choices': [
                        Separator('= News Channels ='),
                        {
                            'name': 'cnn'
                        },
                    {
                            'name': 'bbc-news'
                    },
                    {
                            'name': 'abc-news'
                    },

                    {
                            'name': 'cnbc'

                    },
                ],
                'validate': lambda answer: 'You must choose at least one news source.'
            }
        ]

        answers = prompt(questions, style=style)
        pprint(answers)
        newsource = answers['source']
        pprint(newsource)
        return(newsource)

    def fetch_news_headline(self):
        news_source = self.get_news_channel('NEWS_API_KEY')
        api_key = self.get_api_key()
        url = "{}{}{}{}{},".format("https://newsapi.org/v2/top-headlines?sources=",
                                   news_source, "&apiKey=", api_key, "&pageSize=10")

        headlines = requests.get(url)
        print(headlines)
        if(headlines.ok):

            jData = json.loads(headlines.content)
            data = jData['articles']
           
        return data

    def display_headline(self):
        from __future__ import print_function, unicode_literals

import json
import os
from pprint import pprint

import requests
from PyInquirer import Separator, Token, prompt, style_from_dict
from requests.auth import HTTPDigestAuth

style = style_from_dict(
    {
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454',
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '',
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    }
)


class NewsApi():
    def get_api_key(self):
        return os.getenv("NEWS_API_KEY")

    def get_news_channel(self, api_key):
        if not api_key:
            raise ValueError("Your APi key is missing")

        questions = [
            {
                'type': 'list',
                'message': 'Select news source',
                'name': 'source',
                'choices': [
                        Separator('= News Channels ='),
                        {
                            'name': 'cnn'
                        },
                    {
                            'name': 'bbc-news'
                        },
                    {
                            'name': 'abc-news'
                        },

                    {
                            'name': 'cnbc'

                        },
                ],
                'validate': lambda answer: 'You must choose at least one news source.'
            }
        ]

        answers = prompt(questions, style=style)
        pprint(answers)
        newsource = answers['source']
        pprint(newsource)
        return(newsource)

    def fetch_news_headline(self):
        news_source = self.get_news_channel('NEWS_API_KEY')
        api_key = self.get_api_key()
        url = "{}{}{}{}{},".format("https://newsapi.org/v2/top-headlines?sources=",
                                   news_source, "&apiKey=", api_key, "&pageSize=10")

        headlines = requests.get(url)

        if(headlines.ok):

            jData = json.loads(headlines.content)
            data = jData['articles']

        return data, headlines

    def display_headline(self):

        article_content, headlines = self.fetch_news_headline()
        print(headlines)

        count = 1
        print("The response contains {0} properties".format(
            len(article_content)))
        print("\n")
        for key in article_content:
            print(count)
            print("Title : ", key['title'])
            print("Description : ", key['description'])
            print("Url : ", key['url'])
            count += 1

        article_content = self.fetch_news_headline()
        count = 1
        print("The response contains {0} properties".format(
            len(article_content)))
        print("\n")
        for key in article_content:
            print(count)
            print("Title : ", key['title'])
            print("Description : ", key['description'])
            print("Url : ", key['url'])
            count += 1

    
if __name__ == "__main__":
    news_api = NewsApi()

    news_api.display_headline()
