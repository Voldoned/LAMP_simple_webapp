import requests
import pytest


@pytest.fixture()
def session():
    with requests.Session() as session:
        yield session


@pytest.fixture()
def domen():
    return 'http://app:80'

@pytest.fixture()
def headers_for_requests():
    return {
        'Accept': 'text/html,'
                  'application/json,'
                  'application/xhtml+xml,'
                  'application/xml;q=0.9,'
                  'image/avif,'
                  'image/webp,'
                  'image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'localhost:8000',
        'Sec-Ch-Ua': '"Not.A/Brand";v="8", '
                     '"Chromium";v="114", '
                     '"Google Chrome";v="114"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/114.0.0.0 '
                      'Safari/537.36'
    }