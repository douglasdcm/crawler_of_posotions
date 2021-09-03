from src.crawler import (
    daitan,
    dqrtech,
    mms,
    ciandt,
    cesar,
    generic
)
from src.settings import URLS



class Factory():


    def get_crawlers(self):
        """Retunr the list of enabled crawlers
        Returns:
            (list): list of tuples where the 1st item is the object of the crawler and se 2nd
                informs if it is enable (True). If enabled, the crawler will be executed by the
                server
        """
        crawlers = [
            {
                "company": daitan.Daitan(),
                "url": URLS["Daitan"],
                "enabled": False
            },
            {
                "company": mms.Mms(),
                "url": URLS["Mms"],
                "enabled": False
            },
            {
                "company": dqrtech.Dqrtech(),
                "url": URLS["Dqrtech"],
                "enabled": False
            },
            {
                "company": ciandt.Ciandt(),
                "url": URLS["Ciandt"],
                "enabled": False
            },
            {
                "company": cesar.Cesar(),
                "url": URLS["Cesar"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//div[@class="positions"]//div[@class="container"]//a'),
                "url": URLS["LeroyMerlin"],
                "enabled": False
            },
            {
                # TODO add a specific crawler to consider the pagination of the web page
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Sap"],
                "enabled": False
            },
            {
                # TODO add a specific crawler to consider the pagination of the web page
                "company": generic.Generic(
                    '//span[contains(@class,"hidden-phone")]/a[@class="jobTitle-link"]'),
                "url": URLS["Mars"],
                "enabled": False
            },
            {  # TODO make crawler get just the job description
                "company": generic.Generic(
                    '//div[@class="positions"]//div[@class="container"]//a'),
                "url": URLS["Sabin"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="link"]'),
                "url": URLS["Novarts"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Viacredi"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//td[@data-title="Jobdescription"]/a'),
                "url": URLS["Roche"],
                "enabled": False
            },
            {  # TODO make crawler get just the job description
                "company": generic.Generic(
                    '//div[@class="positions"]//div[@class="container"]//a'),
                "url": URLS["3Coracoes"],
                "enabled": False
            },
            {  # TODO make crawler get the next pages
                "company": generic.Generic(
                    '//div[contains(@class,"search-results__jobinfo")]/a'),
                "url": URLS["3M"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Aeris"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Vivo"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Cielo"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Embraer"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Totvs"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["ViaVarejo"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Gupy"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["GupyTech"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Ambev"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Gpa"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["PicPay"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Randon"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Dasa"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Promob"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Altamogiana"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Vereda"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["PmWeb"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Sicredi"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Cocacola"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Assai"],
                "enabled": False
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["PetLove"],
                "enabled": True
            },
            {
                "company": generic.Generic(
                    '//a[@class="job-list__item"]'),
                "url": URLS["Cotesa"],
                "enabled": False
            },
            # Add new crawlers bellow
        ]
        return crawlers
