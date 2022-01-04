import requests
from prettytable import PrettyTable, ALL
from datetime import datetime, timedelta
import time

try:
    import printer
    import constants
    import config
    import logger
except Exception:
    from startcp import printer, constants, config, logger


logger = logger.Logger()
rangebi = printer.Rangebi()


def utc2local(utc):
    epoch = time.mktime(utc.timetuple())
    offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
    return utc + offset


def print_board():

    contests_board = []

    rangebi.set_spinner(text="fetching contest infos... please wait")
    rangebi.start_spinner()

    # codechef
    contests_json = fetch_contests_by_api(
        constants.contest_board_target_codechef)
    contests_board = parse_contests_json(
        constants.codechef, contests_board, contests_json, 0)

    # codeforces
    contests_json = fetch_contests_by_api(
        constants.contest_board_target_codeforces)
    contests_board = parse_contests_json(
        constants.codeforces, contests_board, contests_json)

    for contest_board in contests_board:
        contest_board.pop(-1)

    rangebi.stop_spinner()
    rangebi.clear_spinner()

    if len(contests_board) > 0:
        print_the_job_board(contests_board)
    else:
        print("Please check your network.")


def fetch_contests_by_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        return ""


def parse_contests_json(target_name, contests_list, contests_json, contest_type=1):

    if contest_type == 1:
        date_format = "%Y-%m-%dT%H:%M:%S."
    else:
        date_format = "%Y-%m-%d %H:%M:%S"

    for contest_json in contests_json:
        contest = []

        contest.append(target_name)

        if contest_json['name'] is not None:
            contest.append(contest_json['name'])
        else:
            contest.append('')

        if (contest_json['start_time'] is not None) and (contest_json['end_time'] is not None):

            start_time_obj_utc = datetime.strptime(
                contest_json['start_time'][:-4], date_format)
            end_time_obj_utc = datetime.strptime(
                contest_json['end_time'][:-4], date_format)

            start_time_local = utc2local(start_time_obj_utc).strftime("%d-%m-%Y - %H:%M")
            end_time_local = utc2local(end_time_obj_utc).strftime("%d-%m-%Y - %H:%M")

            contest.append(start_time_local)
            contest.append(end_time_local)
        else:
            contest.append('')
            contest.append('')

        if contest_json['status'] is not None:
            if contest_json['status'] == "CODING":
                contest.append("LIVE")
            else:
                start_time_obj_utc = datetime.strptime(
                contest_json['start_time'][:-4], date_format)
                start_time_local = utc2local(start_time_obj_utc)
                contest.append(str((start_time_local - datetime.now()))[:-10])

        else:
            contest.append('')

        if contest_json['start_time'] is not None:
            start_time_obj = datetime.strptime(
                contest_json['start_time'][:-4], date_format)
            contest.append(start_time_obj.timestamp())

        contests_list.append(contest)

    return contests_list


def print_the_job_board(contest_board):
    x = PrettyTable()

    x.field_names = ["Target", "Contest",
                     "Start Time", "End Time", "Remaining Time"]

    x.align["Target"] = "l"
    x.align["Contest"] = "l"
    x.align["Start Time"] = "l"
    x.align["End Time"] = "l"
    x.align["Remaining Time"] = "l"

    x._max_width = {
        "Target": 15,
        "Contest": 35,
        "Start Time": 20,
        "End Time": 20,
        "Remaining Time": 15
    }
    x._hrules = ALL

    x.sortby = "Start Time"

    x.add_rows(contest_board)

    print(x)
