import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import threading
import time
import functools

### ANSI Escape Codes ###

# Foreground
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Background
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# Styles
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
UNDERLINE = '\033[4m'
REVERSE = '\033[7m'


### Printing ###

def wait_msg(message):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def print_message():
                print(f"{MAGENTA}{message}{RESET}", end="")
                while not finished.is_set():
                    print(f"{MAGENTA}.{RESET}", end="", flush=True)
                    time.sleep(0.1)
                print()

            finished = threading.Event()
            thread = threading.Thread(target=print_message)
            thread.start()
            try:
                result = func(*args, **kwargs)
                finished.set()
                thread.join()
                print(f"    {GREEN}Done!{RESET}")
                return result
            except Exception as e:
                finished.set()
                thread.join()
                print(f"    {RED}Failed!{RESET}")
                raise e
        return wrapper
    return decorator


### Creating Directory/Files, Pulling Problem Texts/Input ###

def get_aoc_headers():
    script_environment = os.getenv('SCRIPT_ENVIRONMENT', 'local')

    if script_environment == 'github_actions':
        aoc_session_cookie = os.getenv('AOC_SESSION_COOKIE')
    elif script_environment == 'local':
        with open('.aoc_session_cookie', 'r') as file:
            aoc_session_cookie = file.read().strip()

    aoc_headers = {'cookie': f'session={aoc_session_cookie}'}

    return aoc_headers


@wait_msg("Fetching problem 1")
def fetch_problem_1_name_text_url_example(year, day, aoc_headers):
    problem_url = f"https://adventofcode.com/{year}/day/{day}"

    problem_response = requests.get(problem_url, headers=aoc_headers)

    soup = BeautifulSoup(problem_response.text, 'html.parser')

    problem_1_text_full = soup.find('article').get_text()

    example_input = soup.find('pre').find('code').get_text().strip()
    example_solution = soup.find_all('em')[-2].get_text().strip()

    problem_name = problem_1_text_full.split('\n')[0].split(
        ': ')[1].split(' ---')[0].replace(' ', '_')
    problem_1_text = problem_url + "\n\n" + problem_1_text_full.split('---')[2]

    return problem_name, problem_1_text, problem_url, example_input, example_solution


@wait_msg("Fetching input")
def fetch_input_text(year, day, aoc_headers):
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"

    input_response = requests.get(input_url, headers=aoc_headers)

    return input_response.text.strip()


@wait_msg("Fetching problem 2")
def fetch_problem_2_text(year, day, aoc_headers, problem_url):
    problem_url = f"https://adventofcode.com/{year}/day/{day}#part2"

    problem_response = requests.get(problem_url, headers=aoc_headers)

    soup = BeautifulSoup(problem_response.text, 'html.parser')

    problem_2_text = problem_url + "\n\n" + \
        soup.find_all('article')[1].get_text()

    return problem_2_text


def create_day_directory(year, day, problem_name):
    day_dir = f"solutions/{year}/{day}-{problem_name}"
    os.makedirs(day_dir, exist_ok=True)
    return day_dir


def save_text_to_file(text, filename, dirname):
    with open(f"{dirname}/{filename}", 'w') as file:
        file.write(text)


def setup_solution_files_1(dirname, example_solution):
    with open('.language_choice', 'r') as file:
        lang_choice = file.readline().strip().lower()

    if lang_choice == 'python':
        lang_extension = 'py'
        lang_comment = '#'
    elif lang_choice == 'javascript':
        lang_extension = 'js'
        lang_comment = '//'

    os.system(f"cp language-setups/{lang_choice}/solution.{lang_extension} {dirname}/s1.{lang_extension}")
    
    # os.system(f"cp language-setups/{lang_choice}/utils.{lang_extension} {dirname}/utils.{lang_extension}")

    with open(f"{dirname}/s1.{lang_extension}", 'r') as file:
        lines = file.readlines()
        lines.insert(
            len(lines), f"\n{lang_comment} Example Solution: {example_solution}\n")

    with open(f"{dirname}/s1.{lang_extension}", 'w') as file:
        file.writelines(lines)


### Submissions ###

### Testing ###

### Running ###
