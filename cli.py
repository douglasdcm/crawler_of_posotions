"""
CLI function to run the crawlers, compare curriculuns and manage the database.
Try: 'python cli.py --help' for more information.
"""
from logging import basicConfig, INFO
from src.settings import ROOT_DIR, LOG_FILE, RESOURCES_DIR
from sys import argv, path
from src.helper.commands import (
    sanity_check,
    help_,
    overwrite
)
from src.crawler.company import Company
from os import getcwd, system
from dotenv import load_dotenv
from src.helper.helper import Connection


load_dotenv()  # take environment variables from .env.


system('export PATH="{}:$PATH"'.format(RESOURCES_DIR))
path.append(RESOURCES_DIR)
path.append(ROOT_DIR)

basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename=LOG_FILE, level=INFO, datefmt='%Y-%m-%d %H:%M:%S')


def main(*args):
    try:
        for arguments in args:
            if "-h" in arguments or "--help" in arguments:
                output = help_()
                print(output)
                return output
            if "--overwrite" in arguments:
                # Get data from real companies. Not covered by automated testes
                # to avoid overload the real sites
                clean_database = False
                if "--clean-db" in arguments:
                    clean_database = True
                return overwrite(
                    Connection.get_connection_string(),
                    Company().get_all(),
                    clean_database
                )
            elif "--sanity-check" in arguments:
                companies_fake = [{
                    "locator": "//a",
                    "url": "file:///" + getcwd() + "/src/resources/sanity_check.html#",
                    "active": "Y"
                }]
                return sanity_check(Connection.get_connection_string(), companies_fake)
            else:
                print("Invalid command. Try cli.py --help ")
    except Exception as error:
        print(f"Unexpected error. {str(error)}")


if __name__ == '__main__':
    main(argv)
