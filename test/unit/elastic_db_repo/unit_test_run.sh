#!/bin/bash
# Unit testing program for the elastic_db_repo.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  help_message"
test/unit/elastic_db_repo/help_message.py

echo ""
echo "Unit test:  list_dumps"
test/unit/elastic_db_repo/list_dumps.py

echo ""
echo "Unit test:  create_repo"
test/unit/elastic_db_repo/create_repo.py

echo ""
echo "Unit test:  delete_repo"
test/unit/elastic_db_repo/delete_repo.py

echo ""
echo "Unit test:  delete_dump"
test/unit/elastic_db_repo/delete_dump.py

echo ""
echo "Unit test:  rename_repo"
test/unit/elastic_db_repo/rename_repo.py

echo ""
echo "Unit test:  disk_usage"
test/unit/elastic_db_repo/disk_usage.py

echo ""
echo "Unit test:  list_repos"
test/unit/elastic_db_repo/list_repos.py

echo ""
echo "Unit test:  run_program"
test/unit/elastic_db_repo/run_program.py

echo ""
echo "Unit test:  main"
test/unit/elastic_db_repo/main.py

