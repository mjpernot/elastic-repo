# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.

## [0.3.12] - 2024-11-22
- Updated certifi==2024.6.2 for Python 3.
- Updated distro==1.9.0 for Python 3.
- Added idna==2.10 for Python 3.
- Updated urllib3==1.26.19 for Python 3.
- Updated requests==2.25.0 for Python 3.
- Added elastic-transport==8.10.0 for Python 3.
- Updated elasticsearch==8.11.1 for Python 3.
- Updated python-lib to v3.0.8
- Updated elastic-lib to v4.0.7

### Deprecated
- Support for Python 2.7


## [0.3.11] - 2024-09-27
- Updated simplejson==3.13.2 for Python 3
- Updated python-lib to v3.0.5
- Updated elastic-lib to v4.0.5


## [0.3.10] - 2024-08-08
- Updated simplejson==3.13.2
- Updated requests==2.25.0
- Added certifi==2019.11.28
- Added idna==2.10
- Updated elastic-lib to v4.0.4

### Changed
- Updates to requirements.txt.


## [0.3.9] - 2024-08-01
- Set urllib3 to 1.26.19 for Python 2 for security reasons.
- Set requests to 2.22.0 for Python 2
- Updated elastic-lib to v4.0.3

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [0.3.8] - 2024-03-04
- Updated to work in Red Hat 8
- Updated python-lib to v3.0.3
- Updated elastic-lib to v4.0.2

### Changed
- set elasticsearch to 7.17.9 for Python.
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [0.3.7] - 2023-10-05
- Updated to work in Elasticsearch v8.5.2
- Replaced the arg_parser code with gen_class.ArgParser code.

### Changed
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- main, run_program: Removed gen_libs.get_inst call.
- Documentation update


## [0.3.6] - 2022-12-22
- Updated to work in Python 3 too
- Updated elastic-lib to v4.0.1
- Upgraded python-lib to v2.9.4

### Changed
- run_program: Set flavor_id for ProgramLock to "elasticrepo".
- config/elastic.py.TEMPLATE: Set new syntax for host entry.
- requirements.txt: Added certifi==2019.11.28 and updated requests==2.6.0 entries.
- Converted imports to use Python 2.7 or Python 3.
- Documentation update.


## [0.3.5] - 2021-12-01
- Updated to work in Elasticsearch 7.17.0
- Updated elastic-lib to v4.0.0

### Change
- list_dumps:  Pulled only the database dump list from the elastic_class.get_dump_list call.
- delete_dump:  Changed input arguments and output variables to elastic_class.get_dump_list due to elastic_class v4.0.0 update and changed the status check.
- disk_usage:  Changed format of output.
- run_program:  Added connect call, check for elasticsearch connection status, and set login credentials and SSL connection settings.
- config/elastic.py.TEMPLATE:  Added login credentials and SSL entries.
- Removed non-required \*\*kwargs from function calls and parameter lists.
- Documentation updates.


## [0.3.4] - 2020-06-16
### Fixed
- list_dumps, delete_dump:  Changed class attribute name to correct name.
- run_program, main:  Fixed handling command line arguments.
- list_dumps:  Checked for present of repo name in ElasticSearch repository.

### Added
- Add two global print template variables.

### Changed
- run_program, list_repos, disk_usage, rename_repo:  Changed variable name to standard naming convention.
- \_rename, create_repo, delete_repo, delete_dump, list_dumps:  Added global variables and changed variable name to standard naming convention.
- Documentation updates.


## [0.3.3] - 2019-10-31
### Fixed
- run_program:  Fixed error in setting up program lock using incorrect configuration references.
- run_program, rename_repo, delete_dump, delete_repo, create_repo:  Fixed mutable list/dictionary argument issue.

### Added
- \_rename:  Private function for rename_repo().

### Changed
- create_repo:  Repo_name will be joined to repo_dir to create new repository.
- rename_repo:  Replaced part of code with call to \_rename().
- Changed variables to standard naming convention in a number of functions.
- main:  Refactored "if" statements.
- Documentation updates.


## [0.3.2] - 2018-11-22
### Changed
- Documentation updates.


## [0.3.1] - 2018-11-16
### Fixed
- List_dumps option was listing dumps for all repositories even if name of repository was passed to program.
- run_program:  Passed repository name to ElasticSearch instance for List_dumps option.

### Changed
- disk_usage:  Changed print formatting to length of fields.
- Documentation updates.


## [0.3.0] - 2018-10-05
- Field Release.


## [0.2.0] - 2018-08-10
### Changed
- Documentation updates.


## [0.1.4] - 2018-08-03
### Fixed
- list_dumps:  Changed "ER.repo_name" to "ER.repo" to reflect the class attribute setting, changed "ER" to "ER.es" in elastic_class.get_dump_list call to reference internal class instance, replaced "ER.dump_list" with cal to "elastic_class.get_dump_list" function and converted "repo" in "for" loop from unicode to string.


## [0.1.3] - 2018-07-04
Breaking Change

### Changed
- disk_usage, rename_repo, delete_dump, delete_repo, create_repo, list_dumps:  Refactor function to use the new "ElasticSearchRepo" class.
- rename_repo:  Added additional arguments to allow for specific renaming.
- rename_repo:  Added additional checks on arguments being passed to function.
- delete_dump:  Added additional arguments to allow for specific dump deletes.
- main:  Repointed "-R" option to local function:  list_repos.
- run_program:  Changed "ElasticCluster" class to "ElasticSearchRepo" class.

### Added
- list_repos:  Lists the repositories present.


## [0.1.2] - 2018-04-16
Breaking Change

### Changed
- rename_repo, delete_repo:  Replaced "repo_deletion" with "elastic_libs.delete_repo" call.
- list_dumps:  Passed dump list to "elastic_libs.list_dumps" instead of class.
- run_program:  Changed "cfg.name" to "cfg.host".
- Changed "requests_libs" calls to new naming schema.
- rename_repo, create_repo:  Replaced "repo_creation" with "elastic_libs.create_repo" call.
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
- Changed "gen_class" calls to new naming schema.
- Changed "elastic_class" calls to new naming schema.
- Changed "elastic_libs" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.

### Removed
- repo_creation:  Replaced by elastic_libs.create_repo.
- repo_deletion:  Replaced by elastic_libs.delete_repo.


## [0.1.1] - 2018-04-13
### Added
- Added single-source version control.

### Changed
- Changed to use support libraries in sub-directories.


## [0.1.0] - 2017-10-07
- Alpha release.


## [0.0.5] - 2017-10-06
### Added
- main:  Add -U option to display disk usage of dump partition.


## [0.0.4] - 2017-10-05
### Added
- main:  Add option to prevent certain options running at the same time.
- main:  Add -M option to rename a repository.

### Changed
- Create_Repo, Delete_Repo:  Refactored code.

 
## [0.0.3] - 2017-10-04
### Added
- main:  Add -S option to delete dumps in a repository.
- main:  Add -D option to delete a repository.


## [0.0.2] - 2017-10-03
### Added
- main:  Add -C option to create a repository.


## [0.0.1] - 2017-10-03
- Pre-Alpha release.
