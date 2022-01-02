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

    printer.print_header()

    if args.generate:
        generate_start_cp_config_file()
        return
    elif args.version:
        print_version_info()
        return

    operate(args)


def operate(args):
    comp_url = ""

    if args.url:
        comp_url = args.url.lower()
    else:
        printer.new_lines(1)
        printer.print_menu()
        printer.new_lines(1)
        while (True):
            print(
                rangebi.get_in_warning(
                    "(StartCP) $"
                ),
                end=" "
            )
            choices = input().split(" ")

            if choices[0].lower() in ["h", "hlp", "help", "hl"]:
                printer.print_menu()
                print("")
            elif choices[0].lower() in ["e", "exit", "ext", "q", "qt", "quit"]:
                break
            elif choices[0].lower() in ["c", "clr", "clear", "clrscr"]:
                print("clear screen")
            elif choices[0].lower() in ["cp", "comp", "build", "b"]:
                if len(choices) == 1:
                    print(
                        rangebi.get_in_danger("Please give url as second paramter. eg. cp codechef/COMP_ID")
                    )
                    continue
                builder.perform_build(choices[1])


def generate_start_cp_config_file():

    if constants.startcp_config_file.is_file():
        print(
            rangebi.get_in_success(
                "Hey! Config file already generated."
            )
        )
    else:
        start_cp_configuration = constants.default_configuration
        os.makedirs(constants.startcp_default_folder, exist_ok=True)
        with open(str(constants.startcp_config_file), "w") as f:
            f.write(start_cp_configuration)


def print_version_info():
    print("startcp-cli current version:{version_string}".format(version_string=version.string()))
