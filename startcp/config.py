import os
from pathlib import Path
from dotenv import set_key

try:
    import printer
    import constants
    import logger
except Exception:
    from startcp import printer, constants, logger

logger = logger.Logger()


def generate_start_cp_config_file():
    print("Generating startcp config file...")

    IS_SETUP_DONE = None
    PROJECT_PATH = None
    USE_TEMPLATE = None
    MAIN_LANG_TEMPLATE_PATH = None
    BACKUP_LANG_TEMPLATE_PATH = None
    SEPERATE_FOLDER_STRUCTURE_FOR_DIFFERENT_SITES = 1
    CODECHEF_FOLDER_NAME = "Codechef"
    CODEFORCES_FOLDER_NAME = "Codeforces"
    PRACTICE_FOLDER_NAME = "Practice"
    AFTER_GENERATION_COMMAND = None

    while (True):
        print("Do you want to use custom project path? (y/n): ", end="")
        choice = input().lower().strip()
        if choice in ["y", "yes"]:
            IS_SETUP_DONE = 1
            break
        elif choice in ["n", "no"]:
            IS_SETUP_DONE = 0
            break
        else:
            print("Invalid input. Please use y or n.")

    if IS_SETUP_DONE == 1:
        while (True):
            print("Enter project path: ", end="")
            PROJECT_PATH = input().strip()
            if os.path.isdir(PROJECT_PATH):
                break
            else:
                print("Invalid path. Please try again.")

    while (True):
        print("Do you want to use custom template? (y/n): ", end="")
        choice = input().lower().strip()
        if choice in ["y", "yes"]:
            USE_TEMPLATE = 1
            break
        elif choice in ["n", "no"]:
            USE_TEMPLATE = 0
            break
        else:
            print("Invalid input. Please use y or n.")

    if USE_TEMPLATE == 1:
        while (True):
            print("Enter main language template path: ", end="")
            MAIN_LANG_TEMPLATE_PATH = input().strip()
            if Path(MAIN_LANG_TEMPLATE_PATH).is_file():
                break
            else:
                print("Invalid path. Please try again.")

        while (True):
            print("Enter backup language template path: ", end="")
            BACKUP_LANG_TEMPLATE_PATH = input().strip()
            if Path(BACKUP_LANG_TEMPLATE_PATH).is_file():
                break
            else:
                print("Invalid path. Please try again.")

    while (True):
        print("Do you want to run command after generation? (y/n): ", end="")
        choice = input().lower().strip()
        if choice in ["y", "yes"]:
            print("Enter command: ", end="")
            AFTER_GENERATION_COMMAND = input().strip()
            break
        elif choice in ["n", "no"]:
            AFTER_GENERATION_COMMAND = 0
            break
        else:
            print("Invalid input. Please use y or n.")

    start_cp_configuration = """IS_SETUP_DONE = {IS_SETUP_DONE}
PROJECT_PATH = {PROJECT_PATH}
USE_TEMPLATE = {USE_TEMPLATE}
MAIN_LANG_TEMPLATE_PATH = {MAIN_LANG_TEMPLATE_PATH}
BACKUP_LANG_TEMPLATE_PATH = {BACKUP_LANG_TEMPLATE_PATH}
SEPERATE_FOLDER_STRUCTURE_FOR_DIFFERENT_SITES = {SEPERATE_FOLDER_STRUCTURE_FOR_DIFFERENT_SITES}
CODECHEF_FOLDER_NAME = {CODECHEF_FOLDER_NAME}
CODEFORCES_FOLDER_NAME = {CODEFORCES_FOLDER_NAME}
PRACTICE_FOLDER_NAME = {PRACTICE_FOLDER_NAME}
AFTER_GENERATION_COMMAND = {AFTER_GENERATION_COMMAND}""".format(
        IS_SETUP_DONE=IS_SETUP_DONE,
        PROJECT_PATH=PROJECT_PATH,
        USE_TEMPLATE=USE_TEMPLATE,
        MAIN_LANG_TEMPLATE_PATH=MAIN_LANG_TEMPLATE_PATH,
        BACKUP_LANG_TEMPLATE_PATH=BACKUP_LANG_TEMPLATE_PATH,
        SEPERATE_FOLDER_STRUCTURE_FOR_DIFFERENT_SITES=SEPERATE_FOLDER_STRUCTURE_FOR_DIFFERENT_SITES,
        CODECHEF_FOLDER_NAME=CODECHEF_FOLDER_NAME,
        CODEFORCES_FOLDER_NAME=CODEFORCES_FOLDER_NAME,
        PRACTICE_FOLDER_NAME=PRACTICE_FOLDER_NAME,
        AFTER_GENERATION_COMMAND=AFTER_GENERATION_COMMAND
    )

    os.makedirs(constants.startcp_default_folder, exist_ok=True)
    logger.info("Generating default config folder: " +
                constants.startcp_default_folder + " if not exists")
    with open(str(constants.startcp_config_file), "w") as f:
        f.write(start_cp_configuration)
        logger.info("Generating default config file: " +
                    str(constants.startcp_config_file) + " if not exists")
    print("Successfully generated startcp config file. Please restart the application.")


def view_start_cp_config_file():

    print("Viewing startcp config file...")
    printer.new_lines()
    if os.path.isfile(str(constants.startcp_config_file)):
        with open(str(constants.startcp_config_file), "r") as f:
            print(f.read())
    else:
        print("No startcp config file found.")


def check_config_for(constant_name):
    if (not (os.getenv(constant_name) is None)) and (os.getenv(constant_name).strip() != ""):
        return True
    else:
        return False


def get_config_for(constant_name):
    if not (os.getenv(constant_name) is None):
        return os.getenv(constant_name)


def set_config_for(constant_name):
    constant_value = ""
    while (True):
        print("Enter " + constant_name + " (ssh url for better exp): ", end="")
        constant_value = input().strip()
        if not constant_value:
            print("Invalid input. Please try again.")
        else:
            break

    set_key(dotenv_path=constants.startcp_config_file, key_to_set=constant_name,value_to_set=constant_value)
    return True