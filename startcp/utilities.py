import os
from pathlib import Path
import shutil

try:
    import constants
except Exception:
    from startcp import constants


def create_problem_html_file(problem_file_name, problem_url):
    if not os.path.isfile(problem_file_name):
        html_str = get_java_script_code_for_problem(problem_url)

        with open(problem_file_name, "w+") as outfile:
            outfile.write(html_str)


def create_solution_prog_files(problem_folder_name):
    tmplt_file_created = True
    if (not (os.getenv(constants.use_template) is None)) and (int(os.getenv(constants.use_template)) == 1):
        try:
            if not (os.getenv(constants.main_lang_template_path) is None):
                if Path(os.getenv(constants.main_lang_template_path)).is_file():
                    shutil.copy(os.getenv(constants.main_lang_template_path), problem_folder_name + "/")
                    if not (os.getenv(constants.backup_lang_template_path) is None):
                        if Path(os.getenv(constants.backup_lang_template_path)).is_file():
                            shutil.copy(os.getenv(constants.backup_lang_template_path), problem_folder_name + "/")
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

        if not os.path.isfile(problem_folder_name + "/" + "sol.cpp"):
            Path(problem_folder_name + "/" + "sol.cpp").touch()


def create_input_output_files(problem_folder_name, input_str, output_str, file_id):

    input_filename = problem_folder_name + "/" + "in" + str(file_id) + ".txt"
    output_filename = problem_folder_name + "/" + "out" + str(file_id) + ".txt"

    with open(input_filename, "w+") as outfile:
        outfile.write(input_str)
    with open(output_filename, "w+") as outfile:
        outfile.write(output_str)


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
