import os
import re
import json

from pathlib import Path
import shutil

try:
    import constants
    import logger
    import config
    import builder
except Exception:
    from startcp import constants, logger, config, builder

logger = logger.Logger()


def get_competition_id_from_url(target_url, target_regex):
    try:
        return (re.search(re.compile(target_regex), target_url)).group(1)
    except:
        return None


def create_problem_html_file(problem_file_name, problem_url):
    if not os.path.isfile(problem_file_name):
        html_str = get_java_script_code_for_problem(problem_url)
        with open(problem_file_name, "w+") as outfile:
            outfile.write(html_str)
            logger.info("Making if not exists and writing to: " +
                        problem_file_name)


def create_solution_prog_files(problem_folder_name):
    tmplt_file_created = True
    if (not (os.getenv(constants.use_template) is None)) and (int(os.getenv(constants.use_template)) == 1):
        try:
            if not (os.getenv(constants.main_lang_template_path) is None):
                if Path(os.getenv(constants.main_lang_template_path)).is_file():
                    shutil.copy(
                        os.getenv(constants.main_lang_template_path), problem_folder_name + "/")
                    logger.info("Copying from " + os.getenv(constants.main_lang_template_path)
                                + " to " + problem_folder_name)
                    if not (os.getenv(constants.backup_lang_template_path) is None):
                        if Path(os.getenv(constants.backup_lang_template_path)).is_file():
                            shutil.copy(
                                os.getenv(constants.backup_lang_template_path), problem_folder_name + "/")
                            logger.info("Copying from " + os.getenv(constants.backup_lang_template_path)
                                        + " to " + problem_folder_name)
                else:
                    tmplt_file_created = False
            else:
                tmplt_file_created = False
        except Exception:
            tmplt_file_created = False
    else:
        tmplt_file_created = False

    if not tmplt_file_created:
        if not os.path.isfile(problem_folder_name + "/" + "sol.py"):
            Path(problem_folder_name + "/" + "sol.py").touch()
            logger.info("Making if not exists and writing to: " +
                        problem_folder_name + "/" + "sol.py")
        if not os.path.isfile(problem_folder_name + "/" + "sol.cpp"):
            Path(problem_folder_name + "/" + "sol.cpp").touch()
            logger.info("Making if not exists and writing to: " +
                        problem_folder_name + "/" + "sol.cpp")


def create_input_output_files(problem_folder_name, input_str, output_str, file_id):

    input_filename = problem_folder_name + "/" + "in" + str(file_id) + ".txt"
    output_filename = problem_folder_name + "/" + "out" + str(file_id) + ".txt"

    with open(input_filename, "w+") as outfile:
        outfile.write(input_str)
        logger.info("Making if not exists and writing to: " + input_filename)
    with open(output_filename, "w+") as outfile:
        outfile.write(output_str)
        logger.info("Making if not exists and writing to: " + output_filename)


def get_java_script_code_for_problem(problem_url):
    return """
    <html>
        <body>
            <script>
                window.location.replace('{problem_url}');
            </script>
        </body>
    </html>
    """.format(problem_url=problem_url)


def push_current_version_to_github(branch_name):
    try:
        if config.check_config_for(constants.is_setup_done) and int(config.get_config_for(constants.is_setup_done)) == 1:
            curr_dir = os.getcwd()
            os.chdir(config.get_config_for(constants.project_path))
            logger.info("log_msg: " + "Pushing current version to github")
            os.system("git add --all")
            logger.info(
                "log_msg: " + "Pushing current version to github: git add --all")
            os.system("git commit -m \"update\"")
            logger.info(
                "log_msg: " + "Pushing current version to github: git commit -m \"update\"")
            os.system("git push origin " + branch_name)
            logger.info(
                "log_msg: " + "Pushing current version to github: git push origin")
            os.chdir(curr_dir)
        else:
            print(
                "Please generate custom configuration file with project path to use this feature.")

    except Exception as e:
        logger.info("Error while pushing current version to github")


def prepare_for_practice_battlespace(problems_details, platform_id):
    # first moving pointer to the base location of project
    if not builder.move_pointer():
        return

    # creating practice problem folder folder
    if config.check_config_for(constants.practice_folder_name):
        os.makedirs(config.get_config_for(constants.practice_folder_name),
                    exist_ok=True)
        os.chdir(config.get_config_for(constants.practice_folder_name))
        logger.info("Making if not exists and changing directory to: " +
                    config.get_config_for(constants.practice_folder_name))
    else:
        os.makedirs(constants.practice, exist_ok=True)
        os.chdir(constants.practice)
        logger.info(
            "Making if not exists and changing directory to: " + constants.practice)

    for problem_details in problems_details:
        """
        problem_details = {
            "id":"1",
            "from_target":"LEETCODE",
            "title":"TITLE_HERE",
            "difficulty":"HARD",
            "accuracy": xx.yy,
            "url":"PROBLEM_LINK_WITH_BASE_URI",
            "date": datetime_object,
            "status": "IN_PROGRESS"
            "category": "CATEGORY"

        }
        """

        problem_folder_name = problem_details["from_target"] + \
            "_" + problem_details["id"]
        os.makedirs(problem_folder_name, exist_ok=True)

        create_solution_prog_files(problem_folder_name)
        create_problem_html_file(
            problem_folder_name + "/" + "problem.html", problem_details['url']
        )

        if problem_details["from_target"] == constants.leetcode:
            pass
            # leet code is having their own templates which can be integrated later
