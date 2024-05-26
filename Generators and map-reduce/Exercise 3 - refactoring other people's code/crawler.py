import urllib.request
import ssl
import re
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, url):
        self.url = url

    def hack_ssl(self):
        """Ignore certificate errors"""
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    def open_url(self, url):
        """Reads url file as a big string and cleans the html file to make it more readable."""
        ctx = self.hack_ssl()
        html = urllib.request.urlopen(url, context=ctx).read()
        return BeautifulSoup(html, 'html.parser')

    def read_hrefs(self, soup):
        """Get a list of anchor tags, get the href keys and print them."""
        reflist = []
        tags = soup('a')
        for tag in tags:
            reflist.append(tag)
        return reflist

    def read_li(self, soup):
        """Get a list of li tags."""
        lilist = []
        tags = soup('li')
        for tag in tags:
            lilist.append(tag)
        return lilist

    def get_phone(self, info):
        reg = r"(?:(?:00|\+)?[0-9]{4})?(?:[ .-][0-9]{3}){1,5}"
        phone = [s for s in filter(lambda x: 'Telefoon' in str(x), info)]
        try:
            phone = str(phone[0])
        except:
            phone = [s for s in filter(lambda x: re.findall(reg, str(x)), info)]
            try:
                phone = str(phone[0])
            except:
                phone = ""   
        return phone.replace('Facebook', '').replace('Telefoon:', '')

    def get_email(self, soup):
        try: 
            email = [s for s in filter(lambda x: '@' in str(x), soup)]
            email = str(email[0])[4:-5]
            bs = BeautifulSoup(email, features="html.parser")
            email = bs.find('a').attrs['href'].replace('mailto:', '')
        except:
            email = ""
        return email

    def remove_html_tags(self, text):
        """Remove html tags from a string"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def fetch_sidebar(self, soup):
        """Reads html file as a big string and cleans the html file to make it more readable."""
        sidebar = soup.findAll(attrs={'class': 'sidebar'})
        return sidebar[0]

    def extract(self, url):
        text = str(url)
        text = text[26:].split('"')[0] + "/"
        return text

    def crawl_site(self):
        s = self.open_url(self.url)
        reflist = self.read_hrefs(s)
        sub_urls = [s for s in reflist if '<a href="/sportaanbieders' in str(s)][3:]
        print(f'{len(sub_urls)} sub-urls')
        for sub in sub_urls:
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
                print(f'{site} ; {phone} ; {email}')
            except Exception as e:
                print(e)
                exit()
