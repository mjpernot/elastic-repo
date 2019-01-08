#!/bin/bash
# Integration testing program for the elastic_db_repo.py program.
# This will run all the integrations tests for this program.
# Will need to run this from the base directory where the program file
#   is located at.

echo ""
echo "Integration test:  list_dumps"
test/integration/elastic_db_repo/list_dumps.py

echo ""
echo "Integration test:  create_repo"
test/integration/elastic_db_repo/create_repo.py

echo ""
echo "Integration test:  delete_repo"
test/integration/elastic_db_repo/delete_repo.py

echo ""
echo "Integration test:  delete_dump"
test/integration/elastic_db_repo/delete_dump.py

echo ""
echo "Integration test:  rename_repo"
test/integration/elastic_db_repo/rename_repo.py

echo ""
echo "Integration test:  disk_usage"
test/integration/elastic_db_repo/disk_usage.py

echo ""
echo "Integration test:  list_repos"
test/integration/elastic_db_repo/list_repos.py

echo ""
echo "Integration test:  run_program"
test/integration/elastic_db_repo/run_program.py

echo ""
echo "Integration test:  main"
test/integration/elastic_db_repo/main.py

