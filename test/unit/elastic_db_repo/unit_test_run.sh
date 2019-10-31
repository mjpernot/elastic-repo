#!/bin/bash
# Unit testing program for the elastic_db_repo.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test"
test/unit/elastic_db_repo/help_message.py
test/unit/elastic_db_repo/list_dumps.py
test/unit/elastic_db_repo/create_repo.py
test/unit/elastic_db_repo/delete_repo.py
test/unit/elastic_db_repo/delete_dump.py
test/unit/elastic_db_repo/rename_repo.py
test/unit/elastic_db_repo/rename.py
test/unit/elastic_db_repo/disk_usage.py
test/unit/elastic_db_repo/list_repos.py
test/unit/elastic_db_repo/run_program.py
test/unit/elastic_db_repo/main.py

