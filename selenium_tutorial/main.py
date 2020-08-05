# main.py
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


PATH = "C:\\Program Files (x86)\\chromedriver_win32\\chromedriver.exe"


def get_explore_page(page_number):
    return(f'https://www.instagram.com/explore/grid/?is_prefetch=false&omit_cover_media=false&module=explore_popular&use_sectional_payload=true&cluster_id=explore_all%3A0&include_fixed_destinations=true&max_id={page_number}')


def wait_and_find_element(element):
    pass


if __name__ == '__main__':
    with webdriver.Chrome(PATH) as ig_driver:
        wait = WebDriverWait(ig_driver, 5)

        try:
            ig_driver.get('https://www.instagram.com')
            wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        except TimeoutError:
            raise TimeoutError('Timed out loading login page')

        username = ig_driver.find_element_by_name('username')
        username.send_keys('axndr')
        password = ig_driver.find_element_by_name('password')
        password.send_keys('dEq5A9qOrp0I')
        password.send_keys(Keys.RETURN)

        sleep(1)
        # try:
        #     wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        # except TimeoutError:
        #     raise TimeoutError('Timed out loading login page')

        ig_driver.get('https://www.instagram.com/explore')

        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'K6yM_')))
        except TimeoutError:
            raise TimeoutError('Timed out loading explore page')

        posts = ig_driver.find_elements_by_class_name('           QzzMF         Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                            NUiEW  ')
        print(posts.text)
