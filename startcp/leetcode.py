import os
import requests
from datetime import datetime
import webbrowser


try:
    import constants
    import logger
except Exception:
    from startcp import constants, logger


def get_daily_problem():

    problems_details = []
    problem_details = {}

    try:
        payload = {
            "query": constants.leet_code_graphql_payload_daily_problem,
            "variables": {}
        }

        response = requests.post(
            constants.leet_code_graphql_api_endpoint, json=payload)

        if response.status_code == 200:
            response = response.json()
            if response["data"]["activeDailyCodingChallengeQuestion"]:
                problem_details["id"] = response["data"]["activeDailyCodingChallengeQuestion"]["question"]["frontendQuestionId"]
                problem_details["from_target"] = constants.leetcode
                problem_details["title"] = response["data"]["activeDailyCodingChallengeQuestion"]["question"]["title"]
                problem_details["difficulty"] = response["data"]["activeDailyCodingChallengeQuestion"]["question"]["difficulty"]
                problem_details["accuracy"] = response["data"]["activeDailyCodingChallengeQuestion"]["question"]["acRate"]
                problem_details["url"] = constants.leetcode_base_uri + \
                    response["data"]["activeDailyCodingChallengeQuestion"]["link"]
                problem_details["date"] = datetime.strptime(
                    response["data"]["activeDailyCodingChallengeQuestion"]["date"], "%Y-%m-%d").isoformat()

                if response["data"]["activeDailyCodingChallengeQuestion"]["question"]["topicTags"] is not None and len(response["data"]["activeDailyCodingChallengeQuestion"]["question"]["topicTags"]) > 0:
                    problem_details["category"] = response["data"]["activeDailyCodingChallengeQuestion"]["question"]["topicTags"][0]["name"]
                problem_details["status"] = constants.problem_status_in_progress

                webbrowser.open(problem_details["url"])

        problems_details.append(problem_details)

        return problems_details
    except Exception as e:
        print(e)
        return problems_details


def generate_input_output_files(problem_url):
    pass
