import os
import re
import requests

try:
    import printer
    import constants
    import utilities
except Exception:
    from startcp import printer, constants, utilities


rangebi = printer.Rangebi()


def get_codechef_problem_urls(comp_url):
    problem_urls = []

    codechef_comp_id = get_codechef_competition_id(comp_url)
    if not (codechef_comp_id == ""):
        fetch_url = constants.codechef_contest_api_url + codechef_comp_id
        response = requests.get(fetch_url)
        if (response.status_code == 200):
            response = response.json()
            for problem in response["problems"].keys():
                problem_urls.append(
                    fetch_url+response["problems"][problem]["problem_url"])
    return problem_urls


def get_codechef_competition_id(comp_url):
    codechef_validate_re = re.compile(constants.codechef_regex)
    search_result = re.search(codechef_validate_re, comp_url)
    try:
        return search_result.group(1)
    except:
        return ""


def prepare_for_codechef_battle(problem_urls, comp_url):

    if (not (os.getenv(constants.is_setup_done) is None)) and (int(os.getenv(constants.is_setup_done)) == 1):
        if (not (os.getenv(constants.codechef_folder_name) is None)) and (len(os.getenv(constants.codechef_folder_name)) > 0):
            os.makedirs(os.getenv(constants.codechef_folder_name), exist_ok=True)
            os.chdir(os.getenv(constants.codechef_folder_name))
        else:
            os.makedirs(constants.codechef, exist_ok=True)
            os.chdir(constants.codechef)

    codechef_comp_id = get_codechef_competition_id(comp_url)
    os.makedirs(codechef_comp_id, exist_ok=True)
    os.chdir(codechef_comp_id)

    problem_counter = 1
    for problem_url in problem_urls:
        problem_folder_name = str(problem_counter) + "_" + problem_url.split("/")[-1]
        os.makedirs(problem_folder_name, exist_ok=True)

        response = requests.get(problem_url)

        if (response.status_code == 200):

            response = response.json()

            utilities.create_problem_html_file(
                problem_folder_name + "/" + "problem.html",
                comp_url + "/problems/" + problem_url.split("/")[-1]
            )

            utilities.create_solution_prog_files(problem_folder_name)

            for sample_test_case in response["problemComponents"]["sampleTestCases"]:
                id = sample_test_case["id"]
                input_str = sample_test_case["input"]
                output_str = sample_test_case["output"]

                utilities.create_input_output_files(problem_folder_name, input_str, output_str, id)

        problem_counter += 1
