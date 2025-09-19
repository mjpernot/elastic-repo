# Python project for the adminstration of repositories in an Elasticsearch cluster.
# Classification (U)

# Description:
  Used to adminstrate an Elasticsearch repository.  This includes creating, deleting, renaming and listing dumps in a repository.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Create new repositories for Elasticsearch.
  * Removing of repositories.
  * Renaming repositories.
  * List dumps in a repository.
  * Monitoring of disk usage in repositories.


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python3-pip


# Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-repo.git
```

Install/upgrade system modules.

NOTE: Install as the user that will run the program.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```


Install supporting classes and libraries.

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-elastic-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Configuration:

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elasticsearch set up:
    - host = ["https://HOST_NAME1:9200", "https://HOST_NAME2:9200"]

  * If login credentials are required:
    - user = None
    - japd = None

  * If SSL connections are being used:
    - ssl_client_ca = None

```
cp config/elastic.py.TEMPLATE config/elastic.py
chmod 600 config/elastic.py
vim config/elastic.py
sudo chown elasticsearch:elasticsearch config/elastic.py
```


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
elastic_db_repo.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Testing:

```
test/unit/elastic_db_repo/unit_test_run.sh
test/unit/elastic_db_repo/code_coverage.sh
```


# Integration Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Configuration:

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elasticsearch set up:
    - host = ["https://HOST_NAME1:9200", "https://HOST_NAME2:9200"]

  * If login credentials are required:
    - user = None
    - japd = None

  * If SSL connections are being used:
    - ssl_client_ca = None

  * In addition to the normal configuration entries, modify these entries for this testing section.
    Note 1:  **log_repo_dir** is the logical directory path to the share file system.  For use in a Docker set up.
    Note 2:  **phy_repo_dir** is the physical directory path to the share file system.
    Note 3:  If running ElasticSearch as Docker setup, then these two paths will be different.  If running as a standard setup, they will be the same.
    - log_repo_dir = "LOGICAL_DIR_PATH"
    - phy_repo_dir = "PHYSICAL_DIR_PATH"

```
cp test/integration/elastic_db_repo/config/elastic.py.TEMPLATE test/integration/elastic_db_repo/config/elastic.py
chmod 600 test/integration/elastic_db_repo/config/elastic.py
vim test/integration/elastic_db_repo/config/elastic.py
sudo chown elasticsearch:elasticsearch test/integration/elastic_db_repo/config/elastic.py
```

### Testing:
  * These tests must be run as the elasticsearch account:

```
test/integration/elastic_db_repo/integration_test_run.sh
test/integration/elastic_db_repo/code_coverage.sh
```


# Blackbox Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Configuration:

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elasticsearch set up:
    - host = ["https://HOST_NAME1:9200", "https://HOST_NAME2:9200"]

  * If login credentials are required:
    - user = None
    - japd = None

  * If SSL connections are being used:
    - ssl_client_ca = None

```
cp config/elastic.py.TEMPLATE test/blackbox/elastic_db_repo/config/elastic.py
chmod 600 test/blackbox/elastic_db_repo/config/elastic.py
vim test/blackbox/elastic_db_repo/config/elastic.py
sudo chown elasticsearch:elasticsearch test/blackbox/elastic_db_repo/config/elastic.py
```

Setup the test environment for Blackbox testing.
  * Change these entries in the blackbox_test.sh file:
    - REPOSITORY_DIR="DIRECTORY_PATH/TEST_REPO_BLACKBOX_DIR"
  * NOTE:  **DIRECTORY_PATH** is a directory path to a shared file system that is shared and writable by all Elasticsearch databases in the cluster.

```
cp test/blackbox/elastic_db_repo/blackbox_test.sh.TEMPLATE test/blackbox/elastic_db_repo/blackbox_test.sh
vim test/blackbox/elastic_db_repo/blackbox_test.sh
```

### Testing:
  * These tests must be run as the elasticsearch account.

```
test/blackbox/elastic_db_repo/blackbox_test.sh
```

