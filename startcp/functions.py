import json
import requests
import re
import os
from dotenv import load_dotenv, find_dotenv

try:
    import printer
    import constants
    import builder
    import version
except Exception:
    from startcp import printer, constants, builder, version


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

    if args.generate:
        generate_start_cp_config_file()
        return
    elif args.version:
        print_version_info()
        return

    builder.perform_build(args)


def print_version_info():
    print(f"startcp-cli current version: {version.string()}")
