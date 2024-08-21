import logging
import re
import time
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # Import EC correctly
from selenium.webdriver.support.ui import WebDriverWait


def extract_urls(page_number):
    logging.basicConfig(level=logging.INFO)
    # Setup Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    webdriver_service = Service('/home/hamedtbf/Desktop/zoomit-sim/chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    urls = []
    try:
        error_raised = True
        while error_raised:  # Adjust the range as needed
            url = f'https://www.zoomit.ir/archive/?sort=Newest&publishPeriod=All&readingTimeRange=All&pageNumber={page_number}'
            logging.info(f"Loading page {url}")
            try:
                driver.get(url)
                error_raised = False
            except Exception as e:
                logging.error(f"Failed to load {url}: {e}")

        # Wait and extract links
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'a'))
        )
        links = driver.find_elements(By.XPATH, "//a[starts-with(@href, 'https://www.zoomit.ir/')]")

        before = len(urls)

        for link in links:
            if re.match(r'^https://www.zoomit.ir/\w+(-\w+)*/\d+-.+$', link.get_attribute('href')):
                urls.append(link.get_attribute('href'))

        after = len(urls)

        logging.info(f"Extracted {after - before} URLs from {url}")
        time.sleep(1)

    finally:
        driver.quit()
        return urls


def extract_post_id(url):
    id_match = re.search(r'/\d+-', url)
    post_id = url[id_match.start() + 1: id_match.end() - 1]
    return int(post_id)


def extract_title(soup):
    title = soup.find('h1')
    return title.get_text(strip=True)


def extract_content(soup):
    class_ = 'BlockContainer__InnerArticleContainer-s2p0fe-1 hXHdEW'
    start_paragraph = soup.find_all('div', class_=class_)[0].get_text() + ' '
    class_ = 'typography__StyledDynamicTypographyComponent-t787b7-0 fZZfUi ParagraphElement__ParagraphBase-sc-1soo3i3-0 gOVZGU'
    paragraphs = soup.find_all('p', class_=class_)
    text = start_paragraph + ' '.join(paragraph.get_text().strip() for paragraph in paragraphs)
    return text


def extract_tags(soup):
    class_ = 'link__CustomNextLink-sc-1r7l32j-0 cczRGt'
    tags = soup.find_all('a', class_=class_)
    tag_list = []
    for tag in tags:
        class_ = 'typography__StyledDynamicTypographyComponent-t787b7-0 cHbulB'
        if tag.contents[0]['class'] == class_:
            tag_list.append([tag['href'][1:-1], tag.get_text(strip=True)])
    return tag_list


def extract_post_data(url):
    response = None
    error_raised = True
    while error_raised:
        try:
            response = requests.get(url)
            response.raise_for_status()
            error_raised = False
        except HTTPError as er:
            time.sleep(5)
            print(f'{er}\n retrying\n')
    soup = BeautifulSoup(response.text, 'html.parser', multi_valued_attributes=None)

    post_id = extract_post_id(url)
    title = extract_title(soup)
    content = extract_content(soup)
    tags = extract_tags(soup)

    return post_id, title, content, tags


if __name__ == '__main__':
    urls = []
    for page_number in range(1, 5):
        urls.extend(extract_urls(page_number))
    for url in urls:
        data = extract_post_data(url)
