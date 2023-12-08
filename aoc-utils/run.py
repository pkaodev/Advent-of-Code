import os
from datetime import datetime
from utils import get_part_day_year


def run(part, day, year):
    day_dir = f'solutions/{year}/{day}-*'
    file_ext = os.popen(f'ls {day_dir}/s1.*').read().split('.')[-1].strip()
    
    if part == None:
        s2_exists = os.popen(f'ls {day_dir}/s2.*').read()
        if s2_exists:
            part = 2
        else:
            part = 1
    
    if file_ext == 'py':
        run_cmd = 'python3'
    elif file_ext == 'js':
        run_cmd = 'node'
        
    os.system(f'{run_cmd} {day_dir}/s{part}.{file_ext}')


if __name__ == "__main__":
	part, day, year = get_part_day_year()
	run(part, day, year)