# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.3.4] - 2020-06-16
### Fixed
- list_dumps:  Changed class attribute name to correct name.
- delete_dump:  Changed class attribute name to correct name.
- run_program:  Fixed handling command line arguments from SonarQube scan finding.
- main:  Fixed handling command line arguments from SonarQube scan finding.
- list_dumps:  Checked for present of repo name in ElasticSearch repository.

### Added
- Add two global print template variables.

### Changed
- run_program:  Changed variable name to standard naming convention.
- list_repos:  Changed variable name to standard naming convention.
- disk_usage:  Changed variable name to standard naming convention.
- rename_repo:  Changed variable name to standard naming convention.
- \_rename:  Added global variables and changed variable name to standard naming convention.
- create_repo:  Added global variables and changed variable name to standard naming convention.
- delete_repo:  Added global variables and changed variable name to standard naming convention.
- delete_dump:  Added global variables and changed variable name to standard naming convention.
- list_dumps:  Added global variables and changed variable name to standard naming convention.
- Documentation updates.


## [0.3.3] - 2019-10-31
### Fixed
- run_program:  Fixed error in setting up program lock using incorrect configuration references.
- run_program:  Fixed mutable list/dictionary argument issue.
- rename_repo:  Fixed mutable list/dictionary argument issue.
- delete_dump:  Fixed mutable list/dictionary argument issue.
- delete_repo:  Fixed mutable list/dictionary argument issue.
- create_repo:  Fixed mutable list/dictionary argument issue.

### Added
- \_rename:  Private function for rename_repo().

### Changed
- create_repo:  Repo_name will be joined to repo_dir to create new repository.
- rename_repo:  Replaced part of code with call to \_rename().
- run_program:  Changed variables to standard naming convention.
- list_repos:  Changed variables to standard naming convention.
- disk_usage:  Changed variables to standard naming convention.
- rename_repo:  Changed variables to standard naming convention.
- delete_dump:  Changed variables to standard naming convention.
- delete_repo:  Changed variables to standard naming convention.
- create_repo:  Changed variables to standard naming convention.
- list_dumps:  Changed variables to standard naming convention.
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
- list_dumps:  Changed "ER.repo_name" to "ER.repo" to reflect the class attribute setting.
- list_dumps:  Changed "ER" to "ER.es" in elastic_class.get_dump_list call to reference internal class instance.
- list_dumps:  Replaced "ER.dump_list" with cal to "elastic_class.get_dump_list" function.
- list_dumps:  Converted "repo" in "for" loop from unicode to string.


## [0.1.3] - 2018-07-04
Breaking Change

### Changed
- disk_usage:  Refactor function to use the new "ElasticSearchRepo" class.
- rename_repo:  Refactor function to use the new "ElasticSearchRepo" class.
- rename_repo:  Added additional arguments to allow for specific renaming.
- rename_repo:  Added additional checks on arguments being passed to function.
- delete_dump:  Refactor function to use the new "ElasticSearchRepo" class.
- delete_dump:  Added additional arguments to allow for specific dump deletes.
- delete_repo:  Refactor function to use the new "ElasticSearchRepo" class.
- create_repo:  Refactor function to use the new "ElasticSearchRepo" class.
- main:  Repointed "-R" option to local function:  list_repos.
- run_program:  Changed "ElasticCluster" class to "ElasticSearchRepo" class.
- list_dumps:  Refactor function to use the new "ElasticSearchRepo" class.

### Added
- list_repos:  Lists the repositories present.


## [0.1.2] - 2018-04-16
Breaking Change

### Changed
- rename_repo:  Replaced "repo_deletion" with "elastic_libs.delete_repo" call.
- delete_repo:  Replaced "repo_deletion" with "elastic_libs.delete_repo" call.
- list_dumps:  Passed dump list to "elastic_libs.list_dumps" instead of class.
- run_program:  Changed "cfg.name" to "cfg.host".
- Changed "requests_libs" calls to new naming schema.
- rename_repo:  Replaced "repo_creation" with "elastic_libs.create_repo" call.
- create_repo:  Replaced "repo_creation" with "elastic_libs.create_repo" call.
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
- Create_Repo:  Refactored code.
- Delete_Repo:  Refactored code.

 
## [0.0.3] - 2017-10-04
### Added
- main:  Add -S option to delete dumps in a repository.
- main:  Add -D option to delete a repository.


## [0.0.2] - 2017-10-03
### Added
- main:  Add -C option to create a repository.


## [0.0.1] - 2017-10-03
- Pre-Alpha release.
