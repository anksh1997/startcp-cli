from pathlib import Path

# STARTCP CONFIGURATIONS
startcp_default_folder = str(Path.home()) + "/" + "start_cp"
startcp_config_file = Path(startcp_default_folder + "/" + 'startcp_config.env')
startcp_log_file = Path(startcp_default_folder + "/" + 'startcp_transactions.log')
startcp_practice_progress_file = Path(startcp_default_folder + "/" + 'practice_tracking.json')

# END

# CONSTANTS CONFIGURATIONS
is_setup_done = "IS_SETUP_DONE"
project_path = "PROJECT_PATH"
codechef = "CODECHEF"
codeforces = "CODEFORCES"
leetcode = "LEETCODE"
practice = "PRACTICE"
use_template = "USE_TEMPLATE"
main_lang_template_path = "MAIN_LANG_TEMPLATE_PATH"
backup_lang_template_path = "BACKUP_LANG_TEMPLATE_PATH"
seperate_folder_strucutre_enforcement = "SEPERATE_FOLDER_STRUCTURE_FOR_DIFFERENT_SITES"
codechef_folder_name = "CODECHEF_FOLDER_NAME"
codeforces_folder_name = "CODEFORCES_FOLDER_NAME"
practice_folder_name = "PRACTICE_FOLDER_NAME"
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

leet_code_graphql_api_endpoint = "https://leetcode.com/graphql/"
total_daily_problem_endpoints = 1
# END

# BASE URIs
codechef_base_uri = "https://www.codechef.com/"
codeforces_base_uri = "https://www.codeforces.com/contest/"
leetcode_base_uri = "https://leetcode.com"
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

# PAYLOADS
leet_code_graphql_payload_daily_problem = """\n    query questionOfToday {\n  activeDailyCodingChallengeQuestion {\n    date\n    userStatus\n    link\n    question {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      hasVideoSolution\n      hasSolution\n      topicTags {\n        name\n        id\n        slug\n      }\n    }\n  }\n}\n    """
# END

# PROBLEM STATUSES
problem_status_solved = "SOLVED"
problem_status_pending = "PENDING"
problem_status_in_progress = "IN_PROGRESS"
problem_status_skipped = "SKIPPED"
# END
