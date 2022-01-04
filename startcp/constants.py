from pathlib import Path

# STARTCP CONFIGURATIONS
startcp_default_folder = str(Path.home()) + "/" + "start_cp"
startcp_config_file = Path(startcp_default_folder + "/" + 'startcp_config.env')
startcp_log_file = Path(startcp_default_folder + "/" + 'startcp_transactions.log')
# END

# CONSTANTS CONFIGURATIONS
is_setup_done = "IS_SETUP_DONE"
project_path = "PROJECT_PATH"
codechef = "CODECHEF"
codeforces = "CODEFORCES"
use_template = "USE_TEMPLATE"
main_lang_template_path = "MAIN_LANG_TEMPLATE_PATH"
backup_lang_template_path = "BACKUP_LANG_TEMPLATE_PATH"
seperate_folder_strucutre_enforcement = "SEPERATE_FOLDER_STRUCTURE_FOR_DIFFERENT_SITES"
codechef_folder_name = "CODECHEF_FOLDER_NAME"
codeforces_folder_name = "CODEFORCES_FOLDER_NAME"
after_generation_command = "AFTER_GENERATION_COMMAND"
git_repository = "GIT_REPOSITORY"
# END

# API CONFIGURATIONS
codechef_contest_api_url = "https://www.codechef.com/api/contests/"

contest_board_target_codechef = "https://kontests.net/api/v1/code_chef"
contest_board_target_codechef = "https://kontests.net/api/v1/code_chef"
contest_board_target_codeforces = "https://kontests.net/api/v1/codeforces"
contest_board_target_hackerrank = "https://kontests.net/api/v1/hacker_rank"
contest_board_target_hackerearth = "https://kontests.net/api/v1/hacker_earth"
contest_board_target_kickstart = "https://kontests.net/api/v1/kick_start"
contest_board_target_leetcode = "https://kontests.net/api/v1/leet_code"
# END

# BASE URIs
codechef_base_uri = "https://www.codechef.com/"
codeforces_base_uri = "https://www.codeforces.com/contest/"
# END

# REGEX CONFIGURATIONS
# old codechef_regex = r"^https://www.codechef.com/(\w+)(\?.*)?$"
# old codeforces_regex = r"^https://www.codeforces.com/contest/(\w+)(\?.*)?$"
codechef_regex = r"^(?:http(?:s)?://)?(?:www.)?codechef(?:.com)?/(\w+)(\?.*)?$"
codeforces_regex = r"^(?:http(?:s)?://)?(?:www.)?codeforces(?:.com)?/(?:contest/)?(\w+)(\?.*)?$"
# END

# CONFIGURATION
default_configuration = """IS_SETUP_DONE = 0\nPROJECT_PATH = /home/user_name \nUSE_TEMPLATE = 0\nMAIN_LANG_TEMPLATE_PATH = /home/user_name \nBACKUP_LANG_TEMPLATE_PATH = /home/user_name \nSEPERATE_FOLDER_STRUCTURE_FOR_DIFFERENT_SITES = 1\nCODECHEF_FOLDER_NAME = Codechef\nCODEFORCES_FOLDER_NAME = Codeforces\n"""
# END
