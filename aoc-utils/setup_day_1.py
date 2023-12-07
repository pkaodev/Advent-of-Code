import os
from datetime import datetime
from utils import get_aoc_headers, fetch_problem_data, fetch_input, create_day_directory, save_text_to_file, get_lang_choice, create_solution_file


def setup_day_1(year, day):

    aoc_headers = get_aoc_headers()
    
    problem_name, problem_text, problem_url, example_input, example_solution = fetch_problem_data(1, year, day, aoc_headers)
    
    problem_input = fetch_input(year, day, aoc_headers)
    
    day_dir = create_day_directory(year, day, problem_name)
    
    save_text_to_file(problem_text, 'p1.txt', day_dir)
    save_text_to_file(problem_input, 'input', day_dir)
    save_text_to_file(example_input, 'input_example', day_dir)
    
    lang_choice, lang_extension = get_lang_choice()
    
    solution_text = create_solution_file(1, day_dir, lang_choice, example_solution)
    
    save_text_to_file(solution_text, f"s1.{lang_extension}", day_dir)
    
    
if __name__ == "__main__":
    year = os.environ.get('YEAR', datetime.now().year)
    day = os.environ.get('DAY', datetime.now().day)

    setup_day_1(year, day)
