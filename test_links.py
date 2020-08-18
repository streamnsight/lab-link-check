import argparse
import os

import requests
from requests.exceptions import ConnectionError

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

BASE_URL=os.environ.get('BASE_URL')

def collect_links(driver, xpath="//a", attr='href'):
    elements = driver.find_elements_by_xpath(xpath)
    links = []
    for a in elements:
        link = a.get_attribute(attr)
        links.append(link)
    return links

def check_links(links):
    unreachable = []
    for link in links:
        try:
            req = requests.get(link)
            status_code =  req.status_code
            # print(f"{status_code}: {link}")
            if status_code == 404:
                unreachable.append(('not found', link))
        except ConnectionError as e:
            unreachable.append(('connection error', link))
    return unreachable


def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1120, 550)
    print(BASE_URL)
    driver.get(BASE_URL)
    driver.implicitly_wait(3)

    # check the landing page first
    links = collect_links(driver, xpath='//*[@id="contentBox"]//a', attr='href')
    img_links = collect_links(driver, xpath='//img', attr='src')

    # check each other lab page
    print("Checking each lab")
    elements = driver.find_elements_by_xpath('//*[@id="mySidenav"]//li')
    nb_labs = len(elements)
    print(f"scanning {nb_labs} labs")
    for lab in range(1, nb_labs +1):
        element = driver.find_element_by_xpath(f'//*[@id="mySidenav"]//li[{lab}]')
        element.click()
        driver.implicitly_wait(1)
        links += collect_links(driver, xpath='//*[@id="contentBox"]//a', attr='href')
        img_links += collect_links(driver, xpath='//img', attr='src')

    print("UNIQUE LINKS")
    links = list(set(links))
    img_links = list(set(img_links))
    for link in links:
        print(link)
    print("NON-REACHABLE LINKS:")
    unreachable = check_links(links)
    for link in unreachable:
        print(link)

    print("IMAGES NOT FOUND:")
    missing_img = check_links(img_links)
    for link in missing_img:
        print(link)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Test Lab site for missing links')
    parser.add_argument('-b', '--base_url', help='the URL of the landing page for the site')
    args = parser.parse_args()
    url=args.base_url
    if url is not None:
        BASE_URL=url
    if BASE_URL is None:
        parser.print_help()
    else:
        main()