import requests
from bs4 import BeautifulSoup
import csv


def fetch_sitemap_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')

    urls = [elem.text for elem in soup.find_all('loc')]
    return urls


def write_urls_to_csv(urls, filename):
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for url in urls:
            csv_writer.writerow([url])


def update_csv(sitemap_url, filename):
    urls = fetch_sitemap_urls(sitemap_url)
    write_urls_to_csv(urls, filename)


update_csv('https://www.regen.network/sitemap.xml', 'www.csv')
update_csv('https://registry.regen.network/sitemap.xml', 'registry.csv')
update_csv('https://guides.regen.network/sitemap.xml', 'guides.csv')
