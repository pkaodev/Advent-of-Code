.PHONY: setup day

setup:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	@echo "What is your GitHub email?"
	@read email; \
	echo $$email > .gh_login_details
	@echo "What is your GitHub password?"
	@read password; \
	echo $$password >> .gh_login_details

day:
	./venv/bin/python3 pull_daily_problem.py
