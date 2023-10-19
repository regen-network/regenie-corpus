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


def update_sitemap_csv(site):
    urls = fetch_sitemap_urls('https://' + site + '/sitemap.xml')
    filename = 'managed-urls/' + site + '.csv'
    write_urls_to_csv(urls, filename)


def get_github_download_urls(owner, repo, path):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url)

    if response.status_code == 200:
        contents = response.json()
        urls = [item['download_url'] for item in contents if item['download_url'].endswith('.pdf')]
        return urls
    else:
        print(f"Failed with status code: {response.status_code}. Message: {response.text}")


def update_github_download_csv(filename, owner, repo, path):
    urls = get_github_download_urls(owner, repo, path)
    filename = 'managed-urls/' + filename + '.csv'
    write_urls_to_csv(urls, filename)


update_sitemap_csv('docs.regen.network')
update_sitemap_csv('registry.regen.network')
update_sitemap_csv('guides.regen.network')

update_github_download_csv('registry-credit-class-pdfs', 'regen-network', 'regen-registry-credit-classes', '.gitbook/assets')
update_github_download_csv('registry-handbook-pdfs', 'regen-network', 'regen-registry-handbook', '.gitbook/assets')
update_github_download_csv('registry-methodology-pdfs', 'regen-network', 'regen-registry-methodology-library', '.gitbook/assets')
