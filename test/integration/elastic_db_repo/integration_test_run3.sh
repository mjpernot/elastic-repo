#!/bin/bash
# Integration testing program for the elastic_db_repo.py program.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the program file
#   is located at.

echo ""
echo "Integration test"
/usr/bin/python3 test/integration/elastic_db_repo/list_dumps.py
/usr/bin/python3 test/integration/elastic_db_repo/create_repo.py
/usr/bin/python3 test/integration/elastic_db_repo/delete_repo.py
/usr/bin/python3 test/integration/elastic_db_repo/delete_dump.py
/usr/bin/python3 test/integration/elastic_db_repo/rename_repo.py
/usr/bin/python3 test/integration/elastic_db_repo/disk_usage.py
/usr/bin/python3 test/integration/elastic_db_repo/list_repos.py
/usr/bin/python3 test/integration/elastic_db_repo/run_program.py
/usr/bin/python3 test/integration/elastic_db_repo/main.py

