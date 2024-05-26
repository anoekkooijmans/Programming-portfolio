from crawler import Crawler

def main():
    url = "https://sport050.nl/sporten-in-groningen"
    crawler = Crawler(url)
    crawler.crawl_site()

    limited_crawler = zip(range(5), crawler)
    for _, data in limited_crawler:
        print(data)

if __name__ == "__main__":
    main()