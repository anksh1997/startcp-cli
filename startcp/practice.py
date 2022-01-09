import os
import random

try:
    import printer
    import constants
    import utilities
    import leetcode
    import config
    import progress_operator
except Exception:
    from startcp import printer, constants, utilities, leetcode, config, progress_operator


rangebi = printer.Rangebi()


def practice_simulator(show_menu=True):

    if show_menu:
        # one time activity to settle pending problems debt
        progress_operator.settle_pending_problems_debt()

        printer.new_lines()
        print(rangebi.get_in_warning("(StartCP) $ Practice Mode>"))
        print("\t-- 1. Daily Random Problem")
        print("\t-- 2. 5 Random Problem Set")
        print("\t-- 3. Problems According to Category")
        print("\t-- 4. Striver’s SDE Sheet")
        print("\t-- 5. New Problem according to Goldilock's Rule (in R&D)")
        print("\t-- 6. Revisiting solved problems and track progress")
        print("\t-- 0. or exit or back to exit from practice mode")
        printer.new_lines()
    print(rangebi.get_in_warning("(StartCP) $ Practice Mode> "), end="")
    choice = input().strip()

    if choice == "1":
        daily_random_problem()
    elif choice == "2":
        five_random_problem_set()
    elif choice == "3":
        problem_according_to_selected_category()
    elif choice == "4":
        strivers_sde_sheet_next_problem()
    elif choice == "5":
        practice_simulator(False)
    elif choice == "exit" or choice == "back" or choice == "0":
        printer.new_lines()
        return
    else:
        print("Invalid choice. Please try again.")
    printer.new_lines()
    practice_simulator(False)


def daily_random_problem(show_menu=True):
    if show_menu:
        printer.new_lines()
        print(rangebi.get_in_warning(
            "(StartCP) $ Practice Mode> Daily Random Problem> "))
        print("\t\t-- 1. LeetCode")
        print("\t\t-- 2. Codechef")
        print("\t\t-- 0. or exit or back to exit from practice mode")
        printer.new_lines()
    print(rangebi.get_in_warning(
        "(StartCP) $ Practice Mode> Daily Random Problem> "), end="")
    choice = input().strip()

    rangebi.set_spinner("Fetching daily random problem...")
    rangebi.start_spinner()

    if choice == "1":

        problems_details = leetcode.get_daily_problem()
        if len(problems_details) > 0:
            utilities.prepare_for_practice_battlespace(
                problems_details, constants.leetcode)
            progress_operator.add_problems_to_in_progress_state(
                problems_details)
            rangebi.stop_spinner()

            print(rangebi.get_in_success(
                "Success. For leetcode redirecting in the browser."))
            print(rangebi.get_in_success(
                "Practice folder also created in project. Please manually copy the code to backup."))
            if config.check_config_for(constants.after_generation_command):
                os.system(config.get_config_for(
                    constants.after_generation_command))
            else:
                if config.set_config_for(constant_name=constants.after_generation_command):
                    os.system(config.get_config_for(
                        constants.after_generation_command))
            printer.new_lines()

    elif choice == "2":
        rangebi.stop_spinner()
        printer.new_lines()
        pass
    elif choice == "exit" or choice == "back" or choice == "0":
        rangebi.stop_spinner()
        return
    else:
        rangebi.stop_spinner()
        print("Invalid choice. Please try again.")
        printer.new_lines()

    daily_random_problem(False)


def strivers_sde_sheet_next_problem():
    pass


def five_random_problem_set():
    pass


def problem_according_to_selected_category():
    pass
