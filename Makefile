### ANSI Escape Codes ###

# Foreground
RED=\033[31m
GREEN=\033[32m
YELLOW=\033[33m
BLUE=\033[34m
MAGENTA=\033[35m
CYAN=\033[36m
WHITE=\033[37m

# Background
BG_BLACK=\033[40m
BG_RED=\033[41m
BG_GREEN=\033[42m
BG_YELLOW=\033[43m
BG_BLUE=\033[44m
BG_MAGENTA=\033[45m
BG_CYAN=\033[46m
BG_WHITE=\033[47m

# Styles
RESET=\033[0m
BOLD=\033[1m
DIM=\033[2m
UNDERLINE=\033[4m
REVERSE=\033[7m

.PHONY: setup day

setup:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	@echo "$(GREEN)What is your AOC session cookie? (can add to .aoc_session_cookie later)"
	@echo "Instructions on how to get it can be found in README.md$(RESET)"
	@read aoc_session_cookie; \
	echo $$aoc_session_cookie > .aoc_session_cookie

day1:
	./venv/bin/python3 aoc-utils/add_problem_1.py

day2:
	./venv/bin/python3 aoc-utils/add_problem_2.py