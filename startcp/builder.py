import re
import os

try:
    import printer
    import constants
    import codechef
    import codeforces
except Exception:
    from startcp import printer, constants, codechef, codeforces


rangebi = printer.Rangebi()
platform_id = None

def perform_build(args):
    comp_url = ""

    if args.url:
        comp_url = args.url.lower()
        builder.perform_build()
    else:
        printer.new_lines()
        print(
            rangebi.get_in_success(
                "Enter Competition URL:"
            ),
            end=" "
        )
        comp_url = input()
        printer.new_lines()

    if not validate_url(comp_url):
        print(
            rangebi.get_in_danger(
                "URL is not valid. Please try again!"
            )
        )
        printer.new_lines()
        return
    else:
        perform_operations_on_url(comp_url)


def validate_url(comp_url):
    global platform_id

    # regex matching for codechef url
    regex_validator = re.compile(constants.codechef_regex)
    if(re.match(regex_validator, comp_url)):
        platform_id = constants.codechef
        return True

    # regex matching for codeforces url
    regex_validator = re.compile(constants.codeforces_regex)
    if(re.match(regex_validator, comp_url)):
        platform_id = constants.codeforces
        return True

    return False


def perform_operations_on_url(comp_url):
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
        prepare_battlezone(params, comp_url)


def parse_url(comp_url):
    problem_urls = []

    if platform_id == constants.codechef:
        problem_urls = codechef.get_codechef_problem_urls(comp_url)
    elif platform_id == constants.codeforces:
        problem_urls = codeforces.get_codeforces_problem_urls(comp_url)

    return problem_urls


def prepare_battlezone(problem_urls, comp_url):
    move_pointer()

    if platform_id == constants.codechef:
        codechef.prepare_for_codechef_battle(problem_urls, comp_url)
    elif platform_id == constants.codeforces:
        codeforces.prepare_for_codeforces_battle(problem_urls, comp_url)


def move_pointer():
    if (not (os.getenv(constants.is_setup_done) is None)) and (int(os.getenv(constants.is_setup_done)) == 1):
        if not (os.getenv(constants.project_path) is None):
            os.chdir(os.getenv(constants.project_path))
        else:
            os.makedirs(constants.startcp_default_folder, exist_ok=True)
            os.chdir(constants.startcp_default_folder)
    else:
        # lets go home by default
        os.makedirs(constants.startcp_default_folder, exist_ok=True)
        os.chdir(constants.startcp_default_folder)


def generate_start_cp_config_file():

    if constants.startcp_config_file.is_file():
        print(
            rangebi.get_in_success(
                "Hey! Config file already generated."
            )
        )
    else:
        start_cp_configuration = """IS_SETUP_DONE = 0\nPROJECT_PATH = /home/user_name \nUSE_TEMPLATE = 0\nMAIN_LANG_TEMPLATE_PATH = /home/user_name \nBACKUP_LANG_TEMPLATE_PATH = /home/user_name \nSEPERATE_FOLDER_STRUCTURE_FOR_DIFFERENT_SITES = 1\nCODECHEF_FOLDER_NAME = Codechef\nCODEFORCES_FOLDER_NAME = Codeforces\n"""
        os.makedirs(constants.startcp_default_folder, exist_ok=True)
        with open(str(constants.startcp_config_file), "w") as f:
            f.write(start_cp_configuration)