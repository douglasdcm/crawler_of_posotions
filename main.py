"""
Main function to run the crawlers, compare curriculum and manage the database.
Try: 'python main.py --help' for more information.
"""


from logging import basicConfig, INFO
from src.database.db_factory import DbFactory
from src.settings import (ROOT_DIR, LOGS_FILE, RESOURCES_DIR, DB_NAME, DB_TYPE, DRIVER_TYPE)
from src.exceptions.exceptions import ComandoInvalido
from sys import argv, path
from src.helper.commands import install, sanity_check, help_, update
from src.crawler.factory import Factory
from src.crawler.generic import Generic
from os import getcwd, system


system('export PATH="{}:$PATH"'.format(RESOURCES_DIR))
path.append(RESOURCES_DIR)
path.append(ROOT_DIR)

basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOGS_FILE, level=INFO, datefmt='%Y-%m-%d %H:%M:%S')


def main(*args):
    for argumentos in args:
        if "-h" in argumentos or "--help" in argumentos:
            output = help_()
            print(output)
            return output
        if "--initdb" in argumentos:
            return install(DB_NAME, DB_TYPE["p"])
        if "--update" in argumentos:
            df = DbFactory(DB_TYPE["p"])
            db = df.get_db(DB_NAME)
            return update(db, DRIVER_TYPE, Factory().get_crawlers())
        elif "--sanity-check" in argumentos:
            df = DbFactory(DB_TYPE["p"])
            db = df.get_db(DB_NAME)
            crawlers = [{
                "company": Generic("//a"),
                "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
                "enabled": True
            }]
            return sanity_check(db, DRIVER_TYPE, crawlers)
        else:
            raise ComandoInvalido("Invalid command.\nTry main.py --help ")


if __name__ == '__main__':
    main(argv)