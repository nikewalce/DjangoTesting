from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    'тест домашней страницы'
    def test_root_url_resolves_to_home_page_view(self):
        '''корневой url преобразуется в представление домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1, 2)
