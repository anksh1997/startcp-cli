import json
import requests
try:
    from . import printer, constants
except Exception:
    import printer, constants


rangebi = printer.Rangebi()

def run(args):

    comp_url = ''

    if args.url:
        comp_url = args.url.lower()
    else:
        print(
            rangebi.get_in_success(
               "Enter Competition URL:"
            ),
            end=" "
        )
        comp_url = input()

    if not validate_url(comp_url):
        printer.new_lines()
        print(
            rangebi.get_in_danger(
                "URL is not valid. Please try again!"
            )
        )
        printer.new_lines()
        return

    params = parse_url(comp_url)

    if len(params) < 1:
        printer.new_lines()
        print(
            rangebi.get_in_danger(
                "Error parsing the URL!"
            )
        )
        printer.new_lines()
    else:
        prepare_battlezone(params)


def validate_url(comp_url):
    return True


def parse_url(comp_url):

    params = []

    if "codechef" in comp_url.lower():
        comp_url_split = comp_url.split("/")
        params.append(comp_url_split[3])

    return params


def prepare_battlezone(params):



    project_path = ""
    if not constants.is_setup_done:
        print(
            rangebi.get_in_success(
                "Please enter project path:"
            ),
            end=" "
        )
        project_path = input()
    else:
        project_path = constants.project_path
