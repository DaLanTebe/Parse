import requests


def make_request(url, proxy):
    try:
        print(requests.get(url, proxies=proxy).json())
    except Exception as e:
        print(f'Error {e}')

url = 'http://httpbin.org/ip'

proxy_http_https = {
    'http': 'http://103.177.45.3:80',
    'https': 'https://103.177.45.3:80',
}
request = make_request(url, proxy_http_https)

proxy_socks5 = {
    'http': 'socks5://103.177.45.3:80',
    'https': 'socks5://103.177.45.3:80',
}
make_request(url, proxy_socks5)

proxy_with_auth = {
    'http': 'socks5://login:password@103.177.45.3:80',
    'https': 'socks5://login:password@103.177.45.3:80',
}
make_request(url, proxy_with_auth)