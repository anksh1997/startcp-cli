from . import printer

rangebi = printer.Rangebi()

def run(args):

    comp_url = ''

    if args.url:
        comp_url = args.url.lower()
    else:
        print(
            rangebi.get_in_success(
               "Enter Competition URL:"
            ),
            end=" "
        )
        comp_url = input()

    if not validate_url(comp_url):
        printer.new_lines()
        print(
            rangebi.get_in_danger(
                "URL is not valid. Please try again!"
            )
        )
        printer.new_lines()
        return


def validate_url(comp_url):
    return False