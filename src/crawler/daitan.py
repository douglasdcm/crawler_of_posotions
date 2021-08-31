import logging
from src.crawler.icrawler import ICrawler
from src.pages.daitan.vagas import Vagas
import requests
from bs4 import BeautifulSoup as bs


class Daitan(ICrawler):

    def __init__(self):
        self._url = None
        self._vagas = None

    def set_driver(self, driver):
        self._vagas = Vagas(driver)

    def set_url(self, url):
        return super().set_url(url)

    def run(self):
        links = self._get_link_by_browser()
        self._get_info_from_links(links)

    def _save(self, url, description):
        return super()._save(url, description)

    def get_url(self):
        return super().get_url()

    def _get_link_by_browser(self):
        links = []
        next_ = True
        while next_:
            elements = self._vagas.get_link_of_all_positons()
            for element in elements:
                links.append(element)
            next_ = self._vagas.check_next_page_available()
            if next_:
                self._vagas.scroll_to_last_position()
                self._vagas.go_to_next_page()
        return links

    def _get_info_from_links(self, links):
        for link in links:
            page = requests.get(link)
            soup = bs(page.content, 'html.parser')
            result = soup.find_all('li')
            print("===========================")
            print(link)
            logging.info(link)
            descriptions = ""
            for item in result:
                descriptions += item.get_text() + "\n"
            self._save(link, descriptions)
