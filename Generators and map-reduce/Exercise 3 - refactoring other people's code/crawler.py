import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

class Crawler:
    def __init__(self, url):
        self.url = url
        self.current_index = 0
        self.sub_urls = []

    def hack_ssl(self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    def open_url(self, url):
        ctx = self.hack_ssl()
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def read_hrefs(self, soup):
        reflist = [tag for tag in soup('a')]
        return reflist

    def read_li(self, soup):
        lilist = [tag for tag in soup('li')]
        return lilist

    def get_phone(self, info):
        reg = r"(?:(?:00|\+)?[0-9]{4})?(?:[ .-][0-9]{3}){1,5}"
        phone = [str(phone) for phone in filter(lambda x: 'Telefoon' in str(x), info)]
        try:
            phone = phone[0]
        except:
            phone = [str(phone) for phone in filter(lambda x: re.findall(reg, str(x)), info)]
            try:
                phone = phone[0]
            except:
                phone = ""
        return phone.replace('Facebook', '').replace('Telefoon:', '')

    def get_email(self, soup):
        try:
            email = [str(email) for email in filter(lambda x: '@' in str(x), soup)]
            email = str(email[0])[4:-5]
            bs = BeautifulSoup(email, features="html.parser")
            email = bs.find('a').attrs['href'].replace('mailto:', '')
        except:
            email = ""
        return email

    def remove_html_tags(self, text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def fetch_sidebar(self, soup):
        sidebar = soup.find(attrs={'class': 'sidebar'})
        return sidebar

    def extract(self, url):
        text = str(url)
        text = text[26:].split('"')[0] + "/"
        return text

    def crawl_site(self):
        s = self.open_url(self.url)
        reflist = self.read_hrefs(s)
        self.sub_urls = [sub for sub in reflist if '<a href="/sportaanbieders' in str(sub)][3:]

    def crawl_site(self):
        s = self.open_url(self.url)
        reflist = self.read_hrefs(s)
        self.sub_urls = [sub for sub in reflist if '<a href="/sportaanbieders' in str(sub)][3:]

    def __iter__(self):
        return self._crawler_generator()

    def _crawler_generator(self):
        while self.current_index < len(self.sub_urls):
            sub = self.sub_urls[self.current_index]
            try:
                sub = self.extract(sub)
                site = self.url[:-16] + sub
                soup = self.open_url(site)
                info = self.fetch_sidebar(soup)
                info = self.read_li(info)
                phone = self.get_phone(info)
                phone = self.remove_html_tags(phone).strip()
                email = self.get_email(info)
                email = self.remove_html_tags(email).replace("/", "")
                result = f'{site} ; {phone} ; {email}'
                self.current_index += 1
                yield result
            except Exception as e:
                print(e)
                self.current_index += 1
                yield ""
