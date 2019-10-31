#!/bin/bash
# Integration testing program for the elastic_db_repo.py program.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the program file
#   is located at.

echo ""
echo "Integration test"
test/integration/elastic_db_repo/list_dumps.py
test/integration/elastic_db_repo/create_repo.py
test/integration/elastic_db_repo/delete_repo.py
test/integration/elastic_db_repo/delete_dump.py
test/integration/elastic_db_repo/rename_repo.py
test/integration/elastic_db_repo/disk_usage.py
test/integration/elastic_db_repo/list_repos.py
test/integration/elastic_db_repo/run_program.py
test/integration/elastic_db_repo/main.py

