# Python project for the adminstration of repositories in an Elasticsearch cluster.
# Classification (U)

# Description:
  This program is used to adminstrate an Elasticsearch repository.  This includes creating, deleting, renaming and listing dumps in a repository.


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
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/gen_class
    - lib/arg_parser
    - lib/gen_libs
    - elastic_lib/elastic_class
    - elastic_lib/elastic_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-repo.git
```

Install/upgrade system modules.

```
cd elastic-repo
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-requests-lib.txt --target elastic_lib/requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create Elasticsearch configuration file.

```
cd config
cp elastic.py.TEMPLATE elastic.py
```

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elastic.py file.  List all the servers in the Elasticsearch cluster.  Add or delete HOST_NAMEs as necessary.
    - host = ["HOST_NAME1", "HOST_NAME2"]

```
vim elastic.py
chmod 600 elastic.py
sudo chown elasticsearch:elasticsearch elastic.py
```


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/elastic-repo/elastic_db_repo.py -h
```


# Testing:

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the elastic_db_repo.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-repo.git
```

Install/upgrade system modules.

```
cd elastic-repo
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-requests-lib.txt --target elastic_lib/requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit test runs for elastic_db_repo.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/elastic-repo
```

### Unit:  help_message
```
test/unit/elastic_db_repo/help_message.py
```

### Unit:  list_dumps
```
test/unit/elastic_db_repo/list_dumps.py
```

### Unit:  create_repo
```
test/unit/elastic_db_repo/create_repo.py
```

### Unit:  delete_repo
```
test/unit/elastic_db_repo/delete_repo.py
```

### Unit:  delete_dump
```
test/unit/elastic_db_repo/delete_dump.py
```

### Unit:  rename_repo
```
test/unit/elastic_db_repo/rename_repo.py
```

### Unit:  disk_usage
```
test/unit/elastic_db_repo/disk_usage.py
```

### Unit:  list_repos
```
test/unit/elastic_db_repo/list_repos.py
```

### Unit:  run_program
```
test/unit/elastic_db_repo/run_program.py
```

### Unit:  main
```
test/unit/elastic_db_repo/main.py
```

### All unit testing
```
test/unit/elastic_db_repo/unit_test_run.sh
```

### Code coverage program
```
test/unit/elastic_db_repo/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the elastic_db_repo.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-repo.git
```

Install/upgrade system modules.

```
cd elastic-repo
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-requests-lib.txt --target elastic_lib/requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Elasticsearch configuration file.  Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elastic.py file.  List all the servers in the Elasticsearch cluster.  Add or delete HOST_NAMEs as necessary.
    - host = ["HOST_NAME1", "HOST_NAME2"]
    - base_repo_dir = "REPO_DIRECTORY_PATH"
  * NOTE:  **REPO_DIRECTORY_PATH** is a directory path to a shared file system by all Elasticsearch databases in the cluster.

```
cd test/integration/elastic_db_repo/config
cp elastic.py.TEMPLATE elastic.py
vim elastic.py
chmod 600 elastic.py
sudo chown elasticsearch:elasticsearch elastic.py
```

# Integration test runs for elastic_db_repo.py:
  * These tests must be run as the elasticsearch account:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
sudo bash
su - elasticsearch
cd {Python_Project}/elastic-repo
```

### Integration:  list_dumps
```
test/integration/elastic_db_repo/list_dumps.py
```

### Integration:  create_repo
```
test/integration/elastic_db_repo/create_repo.py
```

### Integration:  delete_repo
```
test/integration/elastic_db_repo/delete_repo.py
```

### Integration:  delete_dump
```
test/integration/elastic_db_repo/delete_dump.py
```

### Integration:  rename_repo
```
test/integration/elastic_db_repo/rename_repo.py
```

### Integration:  disk_usage
```
test/integration/elastic_db_repo/disk_usage.py
```

### Integration:  list_repos
```
test/integration/elastic_db_repo/list_repos.py
```

### Integration:  run_program
```
test/integration/elastic_db_repo/run_program.py
```

### Integration:  main
```
test/integration/elastic_db_repo/main.py
```

### All integration testing
```
test/integration/elastic_db_repo/integration_test_run.sh
```

### Code coverage program
```
test/integration/elastic_db_repo/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the elastic_db_repo.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/elastic-repo.git
```

Install/upgrade system modules.

```
cd elastic-repo
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-elastic-lib.txt --target elastic_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target elastic_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-requests-lib.txt --target elastic_lib/requests_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Elasticsearch configuration file.

```
cd test/blackbox/elastic_db_repo/config
cp ../../../../config/elastic.py.TEMPLATE elastic.py
```

Make the appropriate changes to the Elasticsearch environment.
  * Change these entries in the elastic.py file.  List all the servers in the Elasticsearch cluster.  Add or delete HOST_NAMEs as necessary.
    - host = ["HOST_NAME1", "HOST_NAME2"]

```
vim elastic.py
chmod 600 elastic.py
sudo chown elasticsearch:elasticsearch elastic.py
```

Setup the test environment for Blackbox testing.
  * Change these entries in the blackbox_test.sh file:
    - REPOSITORY_DIR="DIRECTORY_PATH/TEST_REPO_BLACKBOX_DIR"
  * NOTE:  **DIRECTORY_PATH** is a directory path to a shared file system that is shared and writable by all Elasticsearch databases in the cluster.

```
cd ..
cp blackbox_test.sh.TEMPLATE blackbox_test.sh
vim blackbox_test.sh
```

# Blackbox test run for elastic_db_repo.py:
  * These tests must be run as the elasticsearch account.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
sudo bash
su - elasticsearch
cd {Python_Project}/elastic-repo
test/blackbox/elastic_db_repo/blackbox_test.sh
```

