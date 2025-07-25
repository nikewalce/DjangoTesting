from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):
    'тест домашней страницы'
    def test_root_url_resolves_to_home_page_view(self):
        '''корневой url преобразуется в представление домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
    
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1, 2)
