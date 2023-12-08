import os
import requests
from utils import get_part_day_year, get_aoc_headers, wait_msg

@wait_msg("Submitting answer")
def submit(answer, part, day, year):
    
	if answer == 'null':
		print('\nNo answer submitted. re-run command as:')
		print('    make submit ANSWER=<answer>')
		return

	day_dir = f'solutions/{year}/{day}-*'
	file_ext = os.popen(f'ls {day_dir}/s1.*').read().split('.')[-1].strip()
  
	if part == None:
		s2_exists = os.popen(f'ls {day_dir}/s2.*').read()
		if s2_exists:
			part = 2
		else:
			part = 1
    
	answer_url = f"https://adventofcode.com/{year}/day/{day}/answer"
	
	post_data = {
            'level' : part,
            'answer' : answer
        }

	headers = get_aoc_headers()
 
	response_text = requests.post(answer_url, headers=headers, data=post_data).text
	
	print(response_text)
 
	# const waitPattern = /You have (.+?) left to wait/;
    # const waitMatch = responseText.match(waitPattern);

	# if (waitMatch !== null) {
	# 	result = 'wait'
	# 	text = `Wait ${waitMatch[1]} before submitting again.`

	# } else if (responseText.includes('Did you already complete it')) {
	# 	result = 'completed'
	# 	text = "You don't seem to be solving the right level.  Did you already complete it?"

	# } else if (responseText.includes('That\'s not the right answer')) {
	# 	result = 'wrong'
	# 	if (responseText.includes('too high')) {
	# 		text = `Your answer, ${answer}, is TOO HIGH.`
	# 	} else if (responseText.includes('too low')) {
	# 		text = `Your answer, ${answer}, is TOO LOW.`
	# 	} else {
	# 		text = `Your answer, ${answer}, is WRONG.`
	# 	}
	# } else if (responseText.includes('That\'s the right answer')) {
	# 	result = 'correct'
	# 	text = `Your answer, ${answer}, is CORRECT!`
	# }

	# console.log("\n", text)

	# if (result==='correct' && part==='1') {
	# 	console.log('pulling part 2')
	# 	exec(`make day2 DAY=${day} YEAR=${year}`, (err, stdout, stderr) => {})
	# }
    
    
if __name__ == "__main__":
	part, day, year = get_part_day_year()
	answer = os.getenv('AOC_ANSWER')
	submit(answer, part, day, year)