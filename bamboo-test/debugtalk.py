import time
import re

from httprunner import __version__

cookies = 'appId=1352475338966638594; Authorization=Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOiIxMzM0NTEyNjUzODU1MDgwNDUwIiwiZW50ZXJwcmlzZU51bWJlciI6IjAwMjUiLCJvcmdhbml6YXRpb25hbElkIjoiNjM3Y2JjYjU1NTNkNDNlOTk3MzFmMGE1Y2Y2NDRmNTIiLCJvcmdhbml6YXRpb25hbE5hbWUiOiLns7vnu5_ov5DokKXpg6giLCJ1c2VyQ2F0ZWdvcnkiOjAsInN1YiI6IuadjuWbvem-mSIsImlzcyI6Im9yZGVycGx1cy1jbGllbnQiLCJpYXQiOjE2MTM5NzI4MDYsImF1ZCI6Im9yZGVycGx1cyIsImV4cCI6MTYxNDU3NzU0NiwibmJmIjoxNjEzOTcyNzQ2fQ.yd1sdbSoNX-V15ElHc_nk90CyNGf1MaL4c8JqD0LY_0;'


def get_httprunner_version():
    return __version__

def sleep(n_secs):
    time.sleep(n_secs)

def sum_two(m, n):
    return m + n

def get_nowtime():
    nowtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    return nowtime

def get_product_name():
    name_str = '测试商品_' 
    name_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    product_name = name_str + name_time

    return product_name

def get_cookies():
    return cookies

def get_authorization():
    cookies = get_cookies()
    Authorization =  re.findall(re.compile('Authorization=(.*?);'),cookies)
    return Authorization[0]

def get_appId():
    cookies = get_cookies()
    appId = re.findall(re.compile('appId=(.*?);'),cookies)
    return appId[0]

# print(get_appId())
# print(get_authorization())
