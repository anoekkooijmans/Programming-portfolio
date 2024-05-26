from crawler import Crawler

if __name__ == "__main__":
    url = "https://sport050.nl/sportaanbieders/alle-aanbieders/"
    crawler = Crawler(url)
    crawler.crawl_site()