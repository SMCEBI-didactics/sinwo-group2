SHELL := /bin/bash

test:
	source tests/start_tests

update-db:
	source tests/update_db

clear:
	rm -rf venv/
