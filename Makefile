.PHONY: setup day

setup:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	@echo "What is your AOC session cookie? (can add to .aoc_session_cookie later)"
	@echo "Instructions on how to get it can be found in README.md"
	@read aoc_session_cookie; \
	echo $$aoc_session_cookie > .aoc_session_cookie

day1:
	./venv/bin/python3 utils/add_problem_1.py

day2:
	./venv/bin/python3 utils/add_problem_2.py