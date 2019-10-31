#!/bin/bash
# Unit test code coverage for elastic_db_repo.py module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/help_message.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/list_dumps.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/create_repo.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/delete_repo.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/delete_dump.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/rename_repo.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/rename.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/disk_usage.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/list_repos.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/run_program.py
coverage run -a --source=elastic_db_repo test/unit/elastic_db_repo/main.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
