import requests
from bs4 import BeautifulSoup
def getText(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.146 Safari/537.36',
    }

    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None
url = 'http://libzw.csu.edu.cn/web/seat3?area=101&segment=1470545&day=2022-10-1&startTime=12:20&endTime=22:00'
html = getText(url)
soup = BeautifulSoup(html,'lxml')


