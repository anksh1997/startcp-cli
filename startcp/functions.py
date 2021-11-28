import json
import requests
import re
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
    # regex matching for codechef url
    codechef_validate_re = re.compile(r"^https://www.codechef.com/(\w+)(\?.*)?$")
    if(re.match(codechef_validate_re,comp_url)):
        return True
    return False

def get_codechef_competition_id(comp_url):
    codechef_validate_re = re.compile(r"^https://www.codechef.com/(\w+)(\?.*)?$")
    search_result = re.search(codechef_validate_re,comp_url)
    try:
        return search_result.group(1)
    except:
        return ""

def parse_url(comp_url):
    problem_urls = []
    codechef_comp_id = get_codechef_competition_id(comp_url)
    if not (codechef_comp_id == "") :
        fetch_url = constants.codechef_contest_api_url + codechef_comp_id
        response = requests.get(fetch_url)
        if (response.status_code == 200):
            response = response.json()
            for problem in response["problems"].keys():
                problem_urls.append(fetch_url+response["problems"][problem]["problem_url"])
    return problem_urls


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
