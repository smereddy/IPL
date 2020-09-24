import requests
from bs4 import BeautifulSoup

class web:

    def __init__(self, url=None):
        self.base_url = 'https://www.sportskeeda.com'
        self.ipl_url = self.base_url + '/go/ipl?page=1'

    def read(self, url):
        s = requests.Session()
        s.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en"
        }
        resp = s.get(url)
        return resp, resp.status_code

    def find_fanatsy(self):
        resp, status_code = self.read(self.ipl_url)
        # http_respone 200 means OK status
        url = None
        if resp.status_code == 200:
            # we need a parser,Python built-in HTML parser is enough .
            soup = BeautifulSoup(resp.text, 'html.parser')
            links = soup.find_all("a")

            for link in links:
                try:
                    if "dream11-team-prediction-fantasy" in link.get("href"):
                        url = link.get("href")
                        break
                except:
                    pass
        else:
            return "Error"

        return url
