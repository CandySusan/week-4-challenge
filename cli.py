from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

import requests
from requests.auth import HTTPDigestAuth
import json

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
    def get_news_channel(self):
        pass


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


url = 'https://newsapi.org/v2/top-headlines?sources='+newsource + \
    '&apiKey=a4d893b3113a4d54bd9ce9bb3d5b96c9&pageSize=10'


myResponse = requests.get(url)

if(myResponse.ok):

    jData = json.loads(myResponse.content)
    data = jData['articles']

    count = 1
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in data:
        print(count)
        print("Title : ", key['title'])
        print("Description : ", key['description'])
        print("Url : ", key['url'])
        count += 1
else:

    myResponse.raise_for_status()
