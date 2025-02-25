#!/usr/bin/python
# Classification (U)

"""Program:  elastic_db_repo.py

    Description:  Runs administration tasks on repositories in an
        Elasticsearch database cluster.

    Usage:
        elastic_db_repo.py -c file -d path
            {-L [repo_name] | -R | -U | -C repo_name -l path | -D repo_name |
             -M old_repo_name new_repo_name | -S dump_name -r repo_name}
            [-v | -h]

    Arguments:
        -c file => Elasticsearch configuration file.  Required argument.
        -d dir path => Directory path for option '-c'.  Required argument.

        -L [repo_name] => List of database dumps for an Elasticsearch
            database.  repo_name is name of repository to dump.  If no repo,
            then all repos and associated dumps will be displayed.

        -R => List of repositories in the Elasticsearch database.

        -U => Display disk usage of any dump partitions.

        -C repo_name => Create new repository name.
            -l path => Directory path name.

        -D repo_name => Delete a repository.

        -M old_repo_name new_repo_name => Rename a repository.

        -S dump_name => Delete dump in a repository.
            -r repo_name => Repository name.

        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and -h overrides all other options.
        NOTE 2:  Options -M, -D, -C, and -S are XOR with all other options.
        NOTE 3:  -U cannot be ran from remote server, must be done locally on
            the Elasticsearch database server.

    Notes:
        Elasticsearch configuration file format (config/elastic.py.TEMPLATE).
        The configuration file format for the Elasticsearch connection to a
        database.

            # Elasticsearch configuration file
            host = ["https://HOST_NAME1:9200", "https://HOST_NAME2:9200"]
            port = 9200

            # Login credentials
            user = None
            japd = None

            # SSL connection
            ssl_client_ca = None
            scheme = "https"

    Example:
        elastic_db_repo.py -c elastic -d config -L Backup_Repo
        elastic_db_repo.py -c elastic -d config -M Backup_Repo New_Backup_Repo

"""

# Libraries and Global Variables

# Standard
import sys
import os

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .elastic_lib import elastic_class
    from .elastic_lib import elastic_libs
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import elastic_lib.elastic_class as elastic_class   # pylint:disable=R0402
    import elastic_lib.elastic_libs as elastic_libs     # pylint:disable=R0402
    import version

__version__ = version.__version__

# Global variables


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def list_dumps(els, **kwargs):                          # pylint:disable=W0613

    """Function:  list_dumps

    Description:  Lists the dumps under a respository or dumps under all
        repositories.

    Arguments:
        (input) els -> ElasticSearch class instance
        (input) **kwargs:
            args -> ArgParser class instance

    """

    repo_list = []

    if els.repo and els.repo in els.repo_dict:
        repo_list.append(els.repo)

    elif els.repo and els.repo not in els.repo_dict:
        print(f"Warning:  Repository {els.repo} does not exist.")

    else:
        repo_list = els.repo_dict

    for repo in repo_list:
        print(f"\nList of Dumps for Reposistory: {str(repo)}")
        elastic_libs.list_dumps(elastic_class.get_dump_list(els.els, repo)[0])


def create_repo(els, repo_name=None, repo_dir=None, **kwargs):

    """Function:  create_repo

    Description:  Create an ElasticSearch repository.

    Arguments:
        (input) els -> ElasticSearch class instance
        (input) repo_name -> Name of repository
        (input) repo_dir -> Repository directory path
        (input) **kwargs:
            args -> ArgParser class instance

    """

    args = kwargs.get("args")

    if not repo_name:
        repo_name = args.get_val("-C")

    if not repo_dir:
        repo_dir = args.get_val("-l")

    if repo_name in els.repo_dict:
        print(f"Error:  {repo_name} repository already exists at: {repo_dir}")

    else:
        err_flag, msg = els.create_repo(
            repo_name, os.path.join(repo_dir, repo_name))

        if err_flag:
            print(f"Error detected for Repository: {repo_name} at {repo_dir}")
            print(f"Reason: {msg}")


def delete_repo(els, repo_name=None, **kwargs):

    """Function:  delete_repo

    Description:  Delete an Elasticsearch repository.

    Arguments:
        (input) els -> ElasticSearch class instance
        (input) repo_name -> Name of repository
        (input) **kwargs:
            args -> ArgParser class instance

    """

    args = kwargs.get("args")

    if not repo_name:
        repo_name = args.get_val("-D")

    if repo_name in els.repo_dict:

        err_flag, msg = els.delete_repo(repo_name)

        if err_flag:
            print(f"Error: Failed to remove repository {repo_name}")
            print(f"Reason: {msg}")

    else:
        print(f"Warning:  Repository {repo_name} does not exist.")


def delete_dump(els, repo_name=None, dump_name=None, **kwargs):

    """Function:  delete_dump

    Description:  Delete a dump in an Elasticsearch repository.

    Arguments:
        (input) els -> ElasticSearch class instance
        (input) repo_name -> Name of repository
        (input) dump_name -> Name of dump to delete
        (input) **kwargs:
            args -> ArgParser class instance

    """

    args = kwargs.get("args")

    if not repo_name:
        repo_name = args.get_val("-r")

    if not dump_name:
        dump_name = args.get_val("-S")

    if repo_name in els.repo_dict:

        dump_list, status, err_msg = elastic_class.get_dump_list(
            els.els, repo_name, snapshot=dump_name)

        if status and dump_list:

            err_flag, msg = els.delete_dump(repo_name, dump_name)

            if err_flag:
                print(f"Error detected for Repository: {repo_name} Dump:"
                      f" {dump_name}")
                print(f"Reason: {msg}")

        else:
            print("Warning: Failed to delete snapshot")
            print(f"Reason: {err_msg}")

    else:
        print(f"Warning:  Repository {repo_name} does not exist.")


def rename_repo(els, name_list=None, **kwargs):

    """Function:  rename_repo

    Description:  Rename an Elasticseatch repository.

    Arguments:
        (input) els -> ElasticSearch class instance
        (input) name_list -> List of two repository names for renaming process
        (input) **kwargs:
            args -> ArgParser class instance

    """

    args = kwargs.get("args")

    if not name_list:
        name_list = list(args.get_val("-M"))

    if isinstance(name_list, list) and len(name_list) == 2:

        if name_list[0] == name_list[1]:
            print(f"Error:  Cannot rename to same name: {name_list}")

        elif name_list[0] not in els.repo_dict:
            print(f"Error:  Source respository {name_list[0]} does not exist")

        elif name_list[1] in els.repo_dict:
            print(f"Error:  Cannot rename to existing repository"
                  f" {name_list[1]}")
        else:
            rename(els, name_list)

    else:
        print(f"Error: Incorrect number of args or is not a list:"
              f" {str(name_list)} ")


def rename(els, name_list):

    """Function:  rename

    Description:  Create new respository and remove old repository.

    Arguments:
        (input) els -> ElasticSearch class instance
        (input) name_list -> List of two repository names for renaming process

    """

    name_list = list(name_list)
    err_flag, msg = els.create_repo(
        name_list[1], els.repo_dict[name_list[0]]["settings"]["location"])

    if err_flag:
        print(f"Error: Unable to rename repository from {name_list[0]} to"
              f" {name_list[1]}")
        print(f"Reason: {msg}")

    else:
        err_flag, msg = els.delete_repo(name_list[0])

        if err_flag:
            print(f"Error: Failed to remove repository {name_list[0]}")
            print(f"Reason: {msg}")


def disk_usage(els, **kwargs):                          # pylint:disable=W0613

    """Function:  disk_usage

    Description:  Display disk usage of dump partitions.

    Arguments:
        (input) els -> ElasticSearch class instance
        (input) **kwargs:
            args -> ArgParser class instance

    """

    if els.repo_dict:
        print(f'{"Total":10} {"Used":10} {"Free":15} {"Percent":10}'
              f' {"Repository":40} {"Partition":65}')

        for repo in els.repo_dict:
            partition = els.repo_dict[repo]["settings"]["location"]
            usage = gen_libs.disk_usage(partition)

            print(f"{gen_libs.bytes_2_readable(usage.total):10}"
                  f" {gen_libs.bytes_2_readable(usage.used):10}"
                  f" {gen_libs.bytes_2_readable(usage.free):10}"
                  f" {(float(usage.used) / usage.total) * 100:10.2f}%"
                  f"     {repo:40} {partition:65}")


def list_repos(els, **kwargs):                          # pylint:disable=W0613

    """Function:  list_repos

    Description:  Lists the repositories present.

    Arguments:
        (input) els -> ElasticSearch class instance
        (input) **kwargs:
            args -> ArgParser class instance

    """

    elastic_libs.list_repos2(els.repo_dict)


def run_program(args, func_dict):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Create a program lock to prevent other instantiations from running.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dictionary list of functions and options

    """

    func_dict = dict(func_dict)
    cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
    user = cfg.user if hasattr(cfg, "user") else None
    japd = cfg.japd if hasattr(cfg, "japd") else None
    ca_cert = cfg.ssl_client_ca if hasattr(cfg, "ssl_client_ca") else None
    scheme = cfg.scheme if hasattr(cfg, "scheme") else "https"
    flavorid = "elasticrepo"

    try:
        prog_lock = gen_class.ProgramLock(sys.argv, flavor_id=flavorid)

        # Find which functions to call.
        for opt in set(args.get_args_keys()) & set(func_dict.keys()):
            els = elastic_class.ElasticSearchRepo(
                cfg.host, port=cfg.port, repo=args.get_val("-L"),
                user=user, japd=japd, ca_cert=ca_cert, scheme=scheme)
            els.connect()

            if els.is_connected:
                func_dict[opt](els, args=args)

            else:
                print("ERROR:  Failed to connect to Elasticsearch")

        del prog_lock

    except gen_class.SingleInstanceException:
        print(f"WARNING:  elastic_db_repo lock in place for: {flavorid}")


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains options which will be directories and the
            octal permission settings
        func_dict -> dictionary list for the function calls or other options
        opt_con_req_dict -> contains options requiring other options
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains options that are required for the program
        opt_val_bin -> List of options that allow 0 or 1 value for option
        opt_val -> contains options which require values
        opt_xor_dict -> contains dict with key that is xor with it's values

    Arguments:
        (input) argv -> Arguments from the command line

    """

    dir_perms_chk = {"-d": 5}
    func_dict = {
        "-L": list_dumps, "-R": list_repos, "-C": create_repo,
        "-D": delete_repo, "-S": delete_dump, "-M": rename_repo,
        "-U": disk_usage}
    opt_con_req_dict = {"-C": ["-l"], "-S": ["-r"]}
    opt_multi_list = ["-M"]
    opt_req_list = ["-c", "-d"]
    opt_val_bin = ["-L"]
    opt_val = ["-c", "-d", "-C", "-l", "-D", "-S", "-r", "-M"]
    opt_xor_dict = {
        "-C": ["-L", "-R", "-S", "-D", "-M", "-U"],
        "-D": ["-L", "-R", "-S", "-C", "-M", "-U"],
        "-S": ["-L", "-R", "-C", "-D", "-M", "-U"],
        "-M": ["-L", "-R", "-S", "-C", "-D", "-U"]}

    # Process argument list from command line.
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val, opt_val_bin=opt_val_bin,
        multi_val=opt_multi_list)

    if args.arg_parse2()                                            \
       and not gen_libs.help_func(args, __version__, help_message)  \
       and args.arg_require(opt_req=opt_req_list)                   \
       and args.arg_xor_dict(opt_xor_val=opt_xor_dict)              \
       and args.arg_cond_req_or(opt_con_or=opt_con_req_dict)        \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk):
        run_program(args, func_dict)


if __name__ == "__main__":
    sys.exit(main())
