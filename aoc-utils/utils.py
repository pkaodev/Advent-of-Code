import os
from datetime import datetime
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
        try:
            with open('.aoc_session_cookie', 'r') as file:
                aoc_session_cookie = file.read().strip()
        except FileNotFoundError:
            aoc_session_cookie = input(f"{A.CYAN}Enter your AoC session cookie {A.MAGENTA}(instructions on how to get it can be found in README.md):{A.RESET}\n ")
            with open('.aoc_session_cookie', 'w') as file:
                file.write(aoc_session_cookie)
            return get_aoc_headers()
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
    problem_name, problem_text, example_input, example_solution = extract_problem_info(part, soup)
    return problem_name, problem_text, problem_url, example_input, example_solution

@wait_msg("Fetching input")
def fetch_input(year, day, headers):
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    return requests.get(input_url, headers=headers).text.strip()

def create_day_directory(year, day, problem_name):
    day_dir = f"solutions/{year}/{day}-{problem_name}"
    os.makedirs(day_dir, exist_ok=True)
    return day_dir

def get_lang_choice():
    with open('.language_choice', 'r') as file:
        lang_choice = file.read().strip()
        
    if lang_choice == 'python':
        lang_extension = 'py'
    elif lang_choice == 'javascript':
        lang_extension = 'js'
        
    return lang_choice, lang_extension

def create_solution_file(part, dirname, lang_choice, example_solution):
    if lang_choice == 'python':
        lang_extension = 'py'
    elif lang_choice == 'javascript':
        lang_extension = 'js'
        
    solution_file_path = f"{dirname}/s{part}.{lang_extension}"
    os.system(f"cp language-setups/{lang_choice}/solution.{lang_extension} {solution_file_path}")

    with open(solution_file_path, 'r') as file:
        lines = file.readlines()

    lines.append(f"{example_solution}")

    return ''.join(lines)

### Running ###
# run1() will run todays p1 file, use .language_choice
# run2()
# run1(day) run2(day)
# run1(day, year) run2(day, year)

### Submitting ###
def get_part_day_year():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.basename(__file__)
    
    part = '1' if '1' in filename else '2'
    day = current_dir.split(os.sep)[-1].split('-')[0]
    year = current_dir.split(os.sep)[-2]

    return part, day, year
    
@wait_msg("Submitting answer")
def submit(answer):
    part, day, year = get_part_day_year()
    problem_url = f"https://adventofcode.com/{year}/day/{day}"
    post_data = {
            'level' : part,
            'answer' : str(answer)
        }
    headers = get_aoc_headers()
    response = requests.post(problem_url, headers=headers, data=post_data)
    print(response.text)
    
    
    
### Testing ###
# def test(part, day=None, year=None):
#     if day is None:
#         day = datetime.now().day
#     if year is None:
#         year = datetime.now().year

    # get language
    # run npm test/pytest on specific file
# same