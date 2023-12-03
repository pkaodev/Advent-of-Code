import requests
from bs4 import BeautifulSoup
from datetime import datetime
import subprocess
import os

GREEN = "\033[92m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def create_directory_for_day(year, dir_name):
    day_dir = f"solutions/{year}/{dir_name}"
    subprocess.run(f'mkdir -p "{day_dir}"', shell=True)
    return day_dir

def save_text_to_file(text, filename):
    with open(filename, 'w') as file:
        file.write(text)

def fetch_problem_text_1(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    problem_text = soup.find('article').get_text()
    return problem_text

def print_day_info(year, day, problem_name):
    subprocess.run('clear', shell=True)
    print(f"{GREEN}Year:{RESET} {MAGENTA}{year}{RESET}\n"
      f"{GREEN}Day:{RESET} {MAGENTA}{day}{RESET}\n"
      f"{GREEN}Problem:{RESET} {MAGENTA}{problem_name}{RESET}")
    
def fetch_and_save_problem_text_2(url, filename, session):
	response = session.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	try:
		problem_text = soup.find_all('article')[1].get_text()
		save_text_to_file(problem_text, filename)
	except IndexError:
		print("Part 2 problem text not found")

def fetch_and_save_input_text(url, filename, session):
    response = session.get(url)
    input_text = response.text
    save_text_to_file(input_text, filename)

def login_to_github_and_authenticate_aoc():
    github_login_url = 'https://github.com/login'
    github_session_url = 'https://github.com/session'
    aoc_gh_auth_url = 'https://adventofcode.com/auth/github'
	
    session = requests.Session()
    
    response = session.get(github_login_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    authenticity_token = soup.find('input', {'name': 'authenticity_token'})['value']
        
    is_github_action = os.getenv('IS_GITHUB_ACTION') == 'true'
    
    if is_github_action:
        gh_email = os.getenv('GH_EMAIL')
        gh_password = os.environ.get('GH_PASSWORD')
     
    else:
        with open('.gh_login_details', 'r') as file:
            gh_email, gh_password = [line.strip() for line in file.readlines()]

    login_data = {
		'login': gh_email,
		'password': gh_password,
		'authenticity_token': authenticity_token
	}

    response = session.post(github_session_url, data=login_data)
    
    if response.ok:
        session.get(aoc_gh_auth_url)
        return session
    else:
        raise Exception("""GitHub login failed
                        response: {response}""")

def main():
    
    year = os.environ.get('YEAR', datetime.now().year)
    day = os.environ.get('DAY', datetime.now().day)

	# Part 1 text
    text_url = f"https://adventofcode.com/{year}/day/{day}"
    problem_text_1 = fetch_problem_text_1(text_url)
 
    problem_name = problem_text_1.split('\n')[0].split(': ')[1].split(' ---')[0].replace(' ', '_')
    day_dir_name = f"{day}-{problem_name}"
 
    print_day_info(year, day, problem_name)
 
	# Create today's directory
    day_dir = create_directory_for_day(year, day_dir_name)

    save_text_to_file(problem_text_1, f"{day_dir}/p1.txt")

	# Part 1 input
    input_url = f"{text_url}/input"
	
    session = login_to_github_and_authenticate_aoc()
		
    fetch_and_save_input_text(input_url, f"{day_dir}/input", session)

	# Part 2 text
    fetch_and_save_problem_text_2(text_url, f"{day_dir}/p2.txt", session)

if __name__ == "__main__":
    main()