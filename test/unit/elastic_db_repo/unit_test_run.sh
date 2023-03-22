#!/bin/bash
# Unit testing program for the elastic_db_repo.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test"
/usr/bin/python test/unit/elastic_db_repo/help_message.py
/usr/bin/python test/unit/elastic_db_repo/list_dumps.py
/usr/bin/python test/unit/elastic_db_repo/create_repo.py
/usr/bin/python test/unit/elastic_db_repo/delete_repo.py
/usr/bin/python test/unit/elastic_db_repo/delete_dump.py
/usr/bin/python test/unit/elastic_db_repo/rename_repo.py
/usr/bin/python test/unit/elastic_db_repo/rename.py
/usr/bin/python test/unit/elastic_db_repo/disk_usage.py
/usr/bin/python test/unit/elastic_db_repo/list_repos.py
/usr/bin/python test/unit/elastic_db_repo/run_program.py
/usr/bin/python test/unit/elastic_db_repo/main.py

