import logging
from src.crawler.icrawler import ICrawler
from src.pages.generic.vagas import Vagas


class Generic(ICrawler):

    def __init__(self, locator):
        """
        This is what the name says: a generic crawler. It is intended to be used if the company's
            page has all the links of positions available in a single page without pagination,
            for example.
            Take the page bellow:
            (...)
                <div class="menu-container">
                    <a class = "menu" herf="www.fake.com">
                </div>
                <div class="positions-container>
                    <a class = "positions" href="www.fake.com/jobs/position_1">
                    <a class = "positions" href="www.fake.com/jobs/position_2">
                    <a class = "positions" href="www.fake.com/jobs/position_3">
                </div>
            (...)
            The locators a.positions (css locator) are the ones we are looking for.
        Arsg:
            locator (str): the locator of the links of positions, e.g. a.positions
        """
        self._url = None
        self._vagas = None
        self.locator = locator

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
        return self._vagas.get_link_of_all_positons(self.locator)

    def _get_info_from_links(self, links):
        for link in links:
            print("===========================")
            print(link)
            logging.info(link)
            self._vagas.go_to_page(link)
            descriptions = self._vagas.get_description()
            self._save(link, descriptions)