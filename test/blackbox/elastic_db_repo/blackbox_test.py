#!/usr/bin/python
# Classification (U)

"""Program:  blackbox_test.py

    Description:  Blackbox testing of elastic_db_repo.py program.

    Usage:
        test/blackbox/elastic_db_repo/blackbox_test.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil

# Third-party

# Local
sys.path.append(os.getcwd())
import lib.gen_libs as gen_libs
import lib.arg_parser as arg_parser
import elastic_lib.elastic_class as elastic_class
import version

__version__ = version.__version__


def load_cfg(args_array):

    """Function:  load_cfg

    Description:  Read and load configuration into cfg.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (output) -> Server configuration settings.

    """

    return gen_libs.load_module(args_array["-c"], args_array["-d"])


def chk_create_repo(els, repo_name):

    """Function:  chk_create_repo

    Description:  Check for the existence of a repository.

    Arguments:
        (input) els -> Elasticsearch class instance.
        (input) repo_name -> Name of repository.
        (output) status -> True|False - Status of check.

    """

    status = True

    if repo_name not in els.repo_dict:
        status = False

    return status


def create_es_instance(cfg, instance, repo_name=None):

    """Function:  create_es_instance

    Description:  Create instance of Elasticsearch database.

    Arguments:
        (input) cfg -> Server configuration settings.
        (input) instance -> ElasticSearch instance name.
        (input) repo_name -> Name of repository.
        (output) -> ElasticSearch instance.

    """

    return instance(cfg.host, cfg.port, repo=repo_name)


def remove_repo(els, repo_name, dump_loc):

    """Function:  remove_repo

    Description:  Remove repository and cleanup directory.

    Arguments:
        (input) els -> ElasticSearchRepo class instance.
        (input) repo_name -> Name of repository being removed.
        (input) dump_loc -> Location of repository.
        (output) status -> True|False - Status of repository removal.

    """

    status = True

    err_flag, msg = els.delete_repo(repo_name=repo_name)

    if err_flag:
        status = False

        print("Error: Failed to remove repo '%s'" % repo_name)
        print("Reason: '%s'" % (msg))

    if os.path.isdir(dump_loc):
        shutil.rmtree(dump_loc)

    return status


def main():

    """Function:  main

    Description:  Control the blackbox testing of elastic_db_dump.py program.

    Variables:
        opt_val_list -> contains options which require values.
        base_dir -> Relative directory path to blackbox testing directory.
        test_path -> Current directory path concatencated with base_dir.
        config_path -> Directory path to blackbox config directory.

    Arguments:

    """

    prt_success = "\n\tTest Successful"
    prt_failure = "\n\tTest Failure"
    cmdline = gen_libs.get_inst(sys)
    opt_val_list = ["-c", "-d", "-n", "-C", "-R", "-S", "-T"]
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list)
    cfg = load_cfg(args_array)

    if "-C" in args_array:
        els = create_es_instance(cfg, elastic_class.ElasticSearchDump,
                                 args_array["-C"])
        elr = create_es_instance(cfg, elastic_class.ElasticSearchRepo,
                                 args_array["-C"])

        if chk_create_repo(elr, args_array["-C"]):
            print(prt_success)

        else:
            print(prt_failure)

        _ = remove_repo(elr, args_array["-C"], els.dump_loc)

    elif "-R" in args_array:
        els = create_es_instance(cfg, elastic_class.ElasticSearchDump,
                                 args_array["-R"])
        elr = create_es_instance(cfg, elastic_class.ElasticSearchRepo,
                                 args_array["-R"])
        _ = remove_repo(elr, args_array["-R"], els.dump_loc)

    elif "-T" in args_array:
        els = create_es_instance(cfg, elastic_class.ElasticSearchDump,
                                 args_array["-T"])
        els.dump_name = args_array["-n"]
        els.dump_db()

    elif "-S" in args_array:
        els = create_es_instance(cfg, elastic_class.ElasticSearchDump,
                                 args_array["-r"])

        if args_array["-S"] in els.dump_list:
            print(prt_failure)

        else:
            print(prt_success)

    elif "-D" in args_array:
        elr = create_es_instance(cfg, elastic_class.ElasticSearchRepo,
                                 args_array["-D"])

        if args_array["-D"] in elr.repo_dict:
            print(prt_failure)

        else:
            print(prt_success)


if __name__ == "__main__":
    sys.exit(main())
