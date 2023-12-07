import os
import requests
import threading
import time
import functools
from bs4 import BeautifulSoup
from ANSI import A

def wait_msg(message):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def print_message():
                print(f"{A.MAGENTA}{message}{A.RESET}", end="")
                while not finished.is_set():
                    print(f"{A.MAGENTA}.{A.RESET}", end="", flush=True)
                    time.sleep(0.1)
                print()

            finished = threading.Event()
            thread = threading.Thread(target=print_message)
            thread.start()
            try:
                result = func(*args, **kwargs)
                finished.set()
                thread.join()
                print(f"    {A.GREEN}Done!{A.RESET}")
                return result
            except Exception as e:
                finished.set()
                thread.join()
                print(f"    {A.RED}Failed!{A.RESET}")
                raise e
        return wrapper
    return decorator

def get_aoc_headers():
    script_environment = os.getenv('SCRIPT_ENVIRONMENT', 'local')
    if script_environment == 'github_actions':
        aoc_session_cookie = os.getenv('AOC_SESSION_COOKIE')
    elif script_environment == 'local':
        with open('.aoc_session_cookie', 'r') as file:
            aoc_session_cookie = file.read().strip()
    return {'cookie': f'session={aoc_session_cookie}'}

def fetch_soup(url, headers):
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, 'html.parser')

def extract_problem_info(part, soup):
    article_1 = soup.find('article')
    problem_name = article_1.get_text().split('\n')[0].split(': ')[1].split(' ---')[0].replace(' ', '_')
    example_input = soup.find('pre').find('code').get_text().strip()
    part_article = soup.find_all('article')[part - 1]
    problem_text = part_article.get_text().split('---')[2]
    example_solution = part_article.find_all('em')[-2].get_text().strip()
    return problem_name, problem_text, example_input, example_solution

def save_text_to_file(text, filename, dirname):
    with open(f"{dirname}/{filename}", 'w') as file:
        file.write(text)

@wait_msg("Fetching problem data")
def fetch_problem_data(part, year, day, headers):
    problem_url = f"https://adventofcode.com/{year}/day/{day}"
    soup = fetch_soup(problem_url, headers)
    if part == 2:
        problem_url += "#part2"
    problem_name, problem_text, example_input, example_solution = extract_problem_info(soup, part)
    return problem_name, problem_text, problem_url, example_input, example_solution

@wait_msg("Fetching input")
def fetch_input(year, day, headers):
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    return requests.get(input_url, headers=headers).text.strip()

def create_day_directory(year, day, problem_name):
    day_dir = f"solutions/{year}/{day}-{problem_name}"
    os.makedirs(day_dir, exist_ok=True)
    return day_dir

def create_solution_file(part, dirname, lang_choice, example_solution):
    if lang_choice == 'python':
        lang_extension = 'py'
        lang_comment = '#'
        lang_solution = f'SOLUTION_{part} = None\n\nprint(f"SOLUTION_{part}: {{SOLUTION_{part}}}")'
    elif lang_choice == 'javascript':
        lang_extension = 'js'
        lang_comment = '//'
        lang_solution = f'const SOLUTION{part} = undefined\n\nconsole.log(`SOLUTION_{part}: ${{SOLUTION_{part}}}`)'

    solution_file_path = f"{dirname}/s{part}.{lang_extension}"
    os.system(f"cp language-setups/{lang_choice}/solution.{lang_extension} {solution_file_path}")

    with open(solution_file_path, 'r') as file:
        lines = file.readlines()

    lines.append(f"\n{lang_solution}\n{lang_comment} Example solution: {example_solution}\n")

    return ''.join(lines)

### Submitting ###
### Testing ###
### Running ###