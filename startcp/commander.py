import os

try:
    import printer
    import constants
    import config
    import contests_board
    import practice
    import builder
    import version
    import utilities
except Exception:
    from startcp import printer, constants, config, contests_board, practice, builder, version, utilities


rangebi = printer.Rangebi()


def command(args):
    comp_url = ""
    try:
        if args.url:
            comp_url = args.url.lower()
        else:
            printer.new_lines()
            printer.print_menu()
            while (True):
                print(
                    rangebi.get_in_warning(
                        "(StartCP) $"
                    ),
                    end=" "
                )

                choices = input().split(" ")

                if choices[0].lower() in ["cp", "comp", "compete"]:
                    if len(choices) == 1:
                        print(
                            rangebi.get_in_danger(
                                "Please give url as second paramter. eg. cp codechef/COMP_ID")
                        )
                        continue
                    if builder.perform_build(choices[1].strip()):
                        print(
                            rangebi.get_in_success(
                                "Successfully prepared for code battle. Good luck!"
                            )
                        )
                        if config.check_config_for(constants.after_generation_command):
                            os.system(config.get_config_for(
                                constants.after_generation_command))
                        else:
                            if config.set_config_for(constant_name=constants.after_generation_command):
                                os.system(config.get_config_for(
                                    constants.after_generation_command))
                elif choices[0].lower() in ["p", "pr", "pract", "practice"]:
                    practice.practice_simulator()
                elif choices[0].lower() in ["board", "b", "contest board", "cb"]:
                    contests_board.print_board()
                elif choices[0].lower() in ["g", "gen", "generate"]:
                    config.generate_start_cp_config_file()
                    break
                elif choices[0].lower() in ["v", "vc", "vw", "view", "viewconfig"]:
                    config.view_start_cp_config_file()
                elif choices[0].lower() in ["git push", "gt", "gp", "push"]:
                    if len(choices) == 1:
                        utilities.push_current_version_to_github("master")
                    else:
                        utilities.push_current_version_to_github(
                            choices[1].strip())
                elif choices[0].lower() in ["h", "hlp", "help", "hl"]:
                    printer.print_menu()
                    print("")
                elif choices[0].lower() in ["c", "clr", "clear", "clrscr"]:
                    print("clear screen implementation in progress")
                elif choices[0].lower() in ["cl", "clear logs"]:
                    print("clear logs implementation in progress")
                elif choices[0].lower() in ["e", "exit", "ext", "q", "qt", "quit"]:
                    break
                else:
                    print("Invalid command. Please use h or help for more info.")
                    printer.new_lines()

    except KeyboardInterrupt:
        print("\nProcess aborted by user. Ctrl + C.")
    except Exception as e:
        print("Error: " + str(e))
        return
