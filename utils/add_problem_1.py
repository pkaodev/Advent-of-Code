import os
from datetime import datetime
from util_functions import get_aoc_headers, fetch_problem_1_name_text_url, fetch_input_text, create_day_directory, save_text_to_file

def add_problem_1(year, day):
    
    aoc_headers = get_aoc_headers()
    
    problem_name, problem_1_text, problem_url = fetch_problem_1_name_text_url(year, day, aoc_headers)
    input_text = fetch_input_text(year, day, aoc_headers)
    
    day_dir = create_day_directory(year, day, problem_name)
    
    save_text_to_file(problem_1_text, 'p1.txt', day_dir)
    save_text_to_file(input_text, 'input', day_dir)
    
if __name__ == "__main__":
    year = os.environ.get('YEAR', datetime.now().year)
    day = os.environ.get('DAY', datetime.now().day)
    
    add_problem_1(year, day)