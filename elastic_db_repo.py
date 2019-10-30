#!/usr/bin/python
# Classification (U)

"""Program:  elastic_db_repo.py

    Description:  Runs administration tasks on repositories in an
        Elasticsearch database cluster.

    Usage:
        elastic_db_repo.py -c file -d path {-L [repo_name] | -R | -U
            | -C repo_name -l path | -D repo_name
            | -M old_repo_name new_repo_name | -S dump_name -r repo_name}
            [-v | -h]

    Arguments:
        -L [repo_name] => List of database dumps for an Elasticsearch
            database.  repo_name is name of repository to dump.  If no repo,
            then all repos and associated dumps will be displayed.
        -R => List of repositories in the Elasticsearch database.
        -D repo_name => Delete a repository.
        -U => Display disk usage of any dump partitions.
        -M old_repo_name new_repo_name => Rename a repository.
        -S dump_name => Delete dump in a repository.  Requires -r option.
        -r repo_name => Repository name.
        -C repo_name => Create new repository name.  Requires -l option.
        -l path => Directory path name.
        -c file => Elasticsearch configuration file.  Required argument.
        -d dir path => Directory path for option '-c'.  Required argument.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and -h overrides all other options.
        NOTE 2:  Options -M, -D, -C, and -S are XOR with all other options.
        NOTE 3:  -U cannot be ran from remote server, must be done locally on
            the Elasticsearch database server.

    Notes:
        Elasticsearch configuration file format (elastic.py).  The
        configuration file format for the Elasticsearch connection to a
        database.

            # Elasticsearch configuration file.
            name = ["HOST_NAME1", "HOST_NAME2"]
            port = PORT_NUMBER (default of Elasticsearch is 9200)

    Example:
        elastic_db_repo.py -c elastic -d config -L Backup_Repo
        elastic_db_repo.py -c elastic -d config -M Backup_Repo New_Backup_Repo

"""

# Libraries and Global Variables

# Standard
import sys

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import elastic_lib.elastic_class as elastic_class
import elastic_lib.elastic_libs as elastic_libs
import version

__version__ = version.__version__


def help_message(**kwargs):

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def list_dumps(ER, **kwargs):

    """Function:  list_dumps

    Description:  Lists the dumps under a respository or dumps under all
        repositories.

    Arguments:
        (input) ER -> ElasticSearch class instance.

    """

    repo_list = []

    if ER.repo:
        repo_list.append(ER.repo)

    else:
        repo_list = ER.repo_dict

    for repo in repo_list:
        print("\nList of Dumps for Reposistory: %s" % (str(repo)))
        elastic_libs.list_dumps(elastic_class.get_dump_list(ER.es, repo))


def create_repo(ER, repo_name=None, repo_dir=None, **kwargs):

    """Function:  create_repo

    Description:  Create an ElasticSearch repository.

    Arguments:
        (input) ER -> ElasticSearch class instance.
        (input) repo_name -> Name of repository.
        (input) repo_dir -> Repository directory path.
        (input) **kwargs:
            args_array -> Dict of command line options and values.

    """

    if not repo_name:
        repo_name = kwargs.get("args_array").get("-C")

    if not repo_dir:
        repo_dir = kwargs.get("args_array").get("-l")

    if repo_name in ER.repo_dict:
        print("Error:  '%s' repository already exists at: '%s'"
              % (repo_name, repo_dir))

    else:
        err_flag, msg = ER.create_repo(repo_name, repo_dir)

        if err_flag:
            print("Error detected for Repository: '%s' at '%s'"
                  % (repo_name, repo_dir))
            print("Reason: '%s'" % (msg))


def delete_repo(ER, repo_name=None, **kwargs):

    """Function:  delete_repo

    Description:  Delete an Elasticsearch repository.

    Arguments:
        (input) ER -> ElasticSearch class instance.
        (input) repo_name -> Name of repository.
        (input) **kwargs:
            args_array -> Dict of command line options and values.

    """

    if not repo_name:
        repo_name = kwargs.get("args_array").get("-D")

    if repo_name in ER.repo_dict:

        err_flag, msg = ER.delete_repo(repo_name)

        if err_flag:
            print("Error: Failed to remove repository '%s'" % (repo_name))
            print("Reason: '%s'" % (msg))

    else:
        print("Warning:  Repository '%s' does not exist." % (repo_name))


def delete_dump(ER, repo_name=None, dump_name=None, **kwargs):

    """Function:  delete_dump

    Description:  Delete a dump in an Elasticsearch repository.

    Arguments:
        (input) ER -> ElasticSearch class instance.
        (input) repo_name -> Name of repository.
        (input) dump_name -> Name of dump to delete.
        (input) **kwargs:
            args_array -> Dict of command line options and values.

    """

    if not repo_name:
        repo_name = kwargs.get("args_array").get("-r")

    if not dump_name:
        dump_name = kwargs.get("args_array").get("-S")

    if repo_name in ER.repo_dict:

        # See if the dump exist
        if any(dump_name == x[0]
               for x in elastic_class.get_dump_list(ER.es, repo_name)):

            err_flag, msg = ER.delete_dump(repo_name, dump_name)

            if err_flag:
                print("Error detected for Repository: '%s' Dump: '%s'"
                      % (repo_name, dump_name))
                print("Reason: '%s'" % (msg))

        else:
            print("Warning:  Dump '%s' does not exist in Repository '%s'"
                  % (dump_name, repo_name))

    else:
        print("Warning:  Repository '%s' does not exist." % (repo_name))


def rename_repo(ER, name_list=None, **kwargs):

    """Function:  rename_repo

    Description:  Rename an Elasticseatch repository.

    Arguments:
        (input) ER -> ElasticSearch class instance.
        (input) name_list -> List of two repository names for renaming process.
        (input) **kwargs:
            args_array -> Dict of command line options and values.

    """

    if not name_list:
        name_list = kwargs.get("args_array").get("-M")

    if isinstance(name_list, list) and len(name_list) == 2:

        if name_list[0] == name_list[1]:
            print("Error:  Cannot rename to same name: %s" % (name_list))

        elif name_list[0] not in ER.repo_dict:
            print("Error:  Source respository '%s' does not exist"
                  % (name_list[0]))

        elif name_list[1] in ER.repo_dict:
            print("Error:  Cannot rename to existing repository '%s'"
                  % (name_list[1]))
        else:
            err_flag, msg = \
                ER.create_repo(
                    name_list[1],
                    ER.repo_dict[name_list[0]]["settings"]["location"])

            if err_flag:
                print("Error: Unable to rename repository from '%s' to '%s'"
                      % (name_list[0], name_list[1]))
                print("Reason: '%s'" % (msg))

            else:
                err_flag, msg = ER.delete_repo(name_list[0])

                if err_flag:
                    print("Error: Failed to remove repository '%s'"
                          % (name_list[0]))
                    print("Reason: '%s'" % (msg))

    else:
        print("Error: Incorrect number of args or is not a list: %s "
              % (str(name_list)))


def disk_usage(ER, **kwargs):

    """Function:  disk_usage

    Description:  Display disk usage of dump partitions.

    Arguments:
        (input) ER -> ElasticSearch class instance.

    """

    if ER.repo_dict:
        print("{0:30} {1:65} {2:10} {3:10} {4:15} {5:10}"
              .format("Repository", "Partition", "Total", "Used", "Free",
                      "Percent"))

        for repo in ER.repo_dict:
            partition = ER.repo_dict[repo]["settings"]["location"]
            usage = gen_libs.disk_usage(partition)

            print("{0:30} {1:65} {2:10} {3:10} {4:10} {5:10.2f}%"
                  .format(repo, partition,
                          gen_libs.bytes_2_readable(usage.total),
                          gen_libs.bytes_2_readable(usage.used),
                          gen_libs.bytes_2_readable(usage.free),
                          (float(usage.used) / usage.total) * 100))


def list_repos(ER, **kwargs):

    """Function:  list_repos

    Description:  Lists the repositories present.

    Arguments:
        (input) ER -> ElasticSearch class instance.

    """

    elastic_libs.list_repos2(ER.repo_dict)


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Create a program lock to prevent other instantiations from running.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.

    """

    cfg = gen_libs.load_module(args_array["-c"], args_array["-d"])

    try:
        PROG_LOCK = gen_class.ProgramLock(sys.argv, cfg.host)

        # Find which functions to call.
        for opt in set(args_array.keys()) & set(func_dict.keys()):
            ER = elastic_class.ElasticSearchRepo(cfg.host, cfg.port,
                                                 repo=args_array.get("-L"))
            func_dict[opt](ER, args_array=args_array, **kwargs)

        del PROG_LOCK

    except gen_class.SingleInstanceException:
        print("WARNING:  elastic_db_repo lock in place for: %s" % (cfg.name))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        func_dict -> dictionary list for the function calls or other options.
        opt_con_req_dict -> contains options requiring other options.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains options that are required for the program.
        opt_val -> List of options that allow 0 or 1 value for option.
        opt_val_list -> contains options which require values.
        opt_xor_dict -> contains dict with key that is xor with it's values.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    dir_chk_list = ["-d"]
    func_dict = {"-L": list_dumps, "-R": list_repos, "-C": create_repo,
                 "-D": delete_repo, "-S": delete_dump, "-M": rename_repo,
                 "-U": disk_usage}
    opt_con_req_dict = {"-C": ["-l"], "-S": ["-r"]}
    opt_multi_list = ["-M"]
    opt_req_list = ["-c", "-d"]
    opt_val = ["-L"]
    opt_val_list = ["-c", "-d", "-C", "-l", "-D", "-S", "-r", "-M"]
    opt_xor_dict = {"-C": ["-L", "-R", "-S", "-D", "-M", "-U"],
                    "-D": ["-L", "-R", "-S", "-C", "-M", "-U"],
                    "-S": ["-L", "-R", "-C", "-D", "-M", "-U"],
                    "-M": ["-L", "-R", "-S", "-C", "-D", "-U"]}

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list,
                                       opt_val=opt_val,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message):
        if not arg_parser.arg_require(args_array, opt_req_list) \
           and arg_parser.arg_xor_dict(args_array, opt_xor_dict) \
           and arg_parser.arg_cond_req_or(args_array, opt_con_req_dict) \
           and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):
            run_program(args_array, func_dict)


if __name__ == "__main__":
    sys.exit(main())
