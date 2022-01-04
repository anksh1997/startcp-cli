import json
import requests
import re
import os

from dotenv import load_dotenv, find_dotenv

try:
    import printer
    import constants
    import commander
    import config
    import version
except Exception:
    from startcp import printer, constants, commander, config, version


rangebi = printer.Rangebi()


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

try:
    if constants.startcp_config_file.is_file():
        load_dotenv(dotenv_path=str(constants.startcp_config_file))
    else:
        load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))
except Exception:
    load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))
    print(rangebi.get_in_info(
        "Custom configuration file not loaded. Please fix the file first."))


def run(args):

    printer.print_header()

    if args.generate:
        config.generate_start_cp_config_file()
        return
    elif args.version:
        print_version_info()
        return

    commander.command(args)


def print_version_info():
    print(
        "startcp-cli current version:{version_string}".format(version_string=version.string()))
