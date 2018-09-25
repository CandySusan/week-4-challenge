import unittest
from cli import NewsApi


class TestNewsApi(unittest.TestCase):
    def setUp(self):
        self.news_api = NewsApi()
        self.api_key = None
    
    def test_api_key_is_available(self):
        with(self.news_api.get_api_key()):
            self.assertRaises(ValueError)

    def test_api_key_is_successfull(self):
        self.assertEqual(self.news_api.get_api_key(),
                         'NEWS_API_KEY')

    def test_number_of_headlines_is_equal_to_10(self):
        self.assertEqual(self.news_api.display_result(), 10)

    def test_data_is_displayed_from_newsapi(self):
        self.assertEqual(self.news_api.check_status_code(), 200)

    def test_user_chooses_news_channel(self):
        self.assertIn(self.news_api.get_news_channel, ('cnbc-news', 'cnbc',
                                                       'bbc-news', 'cnn'))


if __name__ == '__main__':
    unittest.main()
