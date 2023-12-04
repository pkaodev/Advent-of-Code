import os
from datetime import datetime
from utils import get_aoc_headers, fetch_problem_1_name_text_url_example, fetch_problem_2_text, create_day_directory, save_text_to_file


def add_problem_2(year, day):

    aoc_headers = get_aoc_headers()

    problem_name, problem_1_text, problem_url, example_input, example_solution = fetch_problem_1_name_text_url_example(
        year, day, aoc_headers)

    day_dir = create_day_directory(year, day, problem_name)

    problem_2_text = fetch_problem_2_text(year, day, aoc_headers, problem_url)

    save_text_to_file(problem_2_text, 'p2.txt', day_dir)


if __name__ == "__main__":
    year = os.environ.get('YEAR', datetime.now().year)
    day = os.environ.get('DAY', datetime.now().day)

    add_problem_2(year, day)
