from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Book

class BookMethodTests(TestCase):
    def test_recent_pub(self):
        """
        recent_publication()은 False을 미래의 출판 날짜를 위해 반환해야 함
        """
        futuredate = timezone.now().date() + datetime.timedelta(days=5)
        future_pub = Book(publication_date=futuredate)
        self.assertEqual(future_pub.recent_publication(),False)

# import unittest
# from django.test import Client
# class SimpleTest(unittest.TestCase):
#     def test_detatils(self):
#         client = Client()
#         response = client.get('/customer/details/')
#         self.assertEqual(response.status_code,200)
        
#     def test_index(self):
#         client = Client()
#         response = client.get('/customer/index/')
#         self.assertEqual(response.status_code,200)

# 위의 코드를 django.test import TestCase로 변환
# from django.test import TestCase
# class SimpleTest(TestCase):
#     def test_detatils(self):
#         response = self.client.get('/customer/details/')
#         self.assertEqual(response.status_code,200)
        
#     def test_index(self):
#         response = self.client.get('/customer/index/')
#         self.assertEqual(response.status_code,200)

# # settings(), override_settings() 데커레이터
# class LoginTestCase(TestCase):
#     def test_login(self):
#         # 기본 동작에 대한 확인
#         response = self.client.get('/sekrit/')
#         self.assertRedirects(response,'/accounts/login/?next=/sekrit/')
        
#         # LOGIN_URL 설정 재정의(Overriding)
#         with self.settings(LOGIN_URL='/other/login/'):
#             response = self.client.get('/sekrit/')
#             self.assertRedirects(response,'/accounts/login/?next=/sekrit/')
        
#         # LOGIN_URL 설정 원상 복구

# from django.test import override_settings
# class LoginTestCase(TestCase):
#     @override_settings(LOGIN_URL='/other/login/')
#     def test_login(self):
#         response = self.client.get('/sekrit/')
#         self.assertRedirects(response,'/accounts/login/?next=/sekrit/')

# # modify_setting(), modify_setting() 데커레이터
# from django.test import TestCase

# class MiddlewareTestCase(TestCase):

#     def test_cache_middleware(self):
#         MIDDLEWARE_CLASSES = {
#         'append':'django.middleware.cache.FetchFromCacheMiddleWare',
#         'prepend':'django.middleware.cache.UpdateCacheMiddleware',
#         'remove':[
#         'django.contrib.sessions.middleware.SessionMiddleware',
#         'django.contrib.auth.middleware.AuthenticationMiddleware',
#         'django.contrib.messages.middleware.MessageMiddleware',
#         ],
#         }
#         with self.modify_settings(MIDDLEWARE_CLASSES):
#             response = self.client.get('/')
#             # ...
# from django.test import TestCase, modify_settings

# @modify_settings(MIDDLEWARE_CLASSES = {
#         'append':'django.middleware.cache.FetchFromCacheMiddleWare',
#         'prepend':'django.middleware.cache.UpdateCacheMiddleware',
#         'remove':[
#         'django.contrib.sessions.middleware.SessionMiddleware',
#         'django.contrib.auth.middleware.AuthenticationMiddleware',
#         'django.contrib.messages.middleware.MessageMiddleware',
#         ],}
# )
# class MiddlewareTestCase(TestCase):

#     def test_cache_middleware(self):
#         response = self.client.get('/')
#         # ...