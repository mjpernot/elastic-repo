# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/run_program.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_repo
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def disk_usage(els, **kwargs):

    """Function:  disk_usage

    Description:  This is a function stub for elastic_db_repo.disk_usage.

    Arguments:

    """

    status = True

    if els and kwargs.get("args"):
        status = True

    return status


def list_repos(els, **kwargs):

    """Function:  list_repos

    Description:  This is a function stub for elastic_db_repo.list_repos.

    Arguments:

    """

    status = True

    if els and kwargs.get("args"):
        status = True

    return status


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val
        get_args_keys

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "mongo_cfg", "-d": "config"}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = cmdline
        self.flavor = flavor


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.host = ["SERVER_NAME"]
        self.port = 9200
        self.user = None
        self.japd = None
        self.ssl_client_ca = None
        self.scheme = "https"


class ElasticSearchRepo(object):

    """Class:  ElasticSearchRepo

    Description:  Class stub holder for elastic_class.ElasticSearchRepo class.

    Methods:
        __init__
        connect

    """

    def __init__(self, host, port, repo, user, japd, ca_cert, scheme):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.host = host
        self.port = port
        self.repo = repo
        self.user = user
        self.japd = japd
        self.ca_cert = ca_cert
        self.scheme = scheme
        self.is_connected = True

    def connect(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_programlock_id
        test_exception_handler
        test_func_call_multi
        test_func_call_one
        test_func_call_zero

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.args = ArgParser()
        self.args.args_array = {
            "-c": "config_file", "-d": "config_dir", "-M": True}
        self.func_names = {"-U": disk_usage, "-R": list_repos}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")
        self.elr = ElasticSearchRepo(
            self.cfg.host, self.cfg.port, None, self.cfg.user,
            self.cfg.japd, self.cfg.ssl_client_ca, self.cfg.scheme)

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_failed_connection(self, mock_lock, mock_class, mock_load):

        """Function:  test_failed_connection

        Description:  Test with failed connection.

        Arguments:

        """

        self.args.args_array["-U"] = True
        self.elr.is_connected = False

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.elr
        mock_load.return_value = self.cfg

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.run_program(self.args, self.func_names))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_success_connection(self, mock_lock, mock_class, mock_load):

        """Function:  test_success_connection

        Description:  Test with successful connection.

        Arguments:

        """

        self.args.args_array["-U"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.elr
        mock_load.return_value = self.cfg

        self.assertFalse(
            elastic_db_repo.run_program(self.args, self.func_names))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_programlock_id(self, mock_lock, mock_class, mock_load):

        """Function:  test_programlock_id

        Description:  Test ProgramLock with flavor ID.

        Arguments:

        """

        self.args.args_array["-U"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.elr
        mock_load.return_value = self.cfg

        self.assertFalse(
            elastic_db_repo.run_program(self.args, self.func_names))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_exception_handler(self, mock_lock, mock_class, mock_load):

        """Function:  test_exception_handler

        Description:  Test with exception handler.

        Arguments:

        """

        self.args.args_array["-U"] = True

        mock_lock.side_effect = \
            elastic_db_repo.gen_class.SingleInstanceException
        mock_class.return_value = self.elr
        mock_load.return_value = self.cfg

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.run_program(self.args, self.func_names))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_func_call_multi(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_multi

        Description:  Test run_program function with multiple calls to
            function.

        Arguments:

        """

        self.args.args_array["-U"] = True
        self.args.args_array["-R"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.elr
        mock_load.return_value = self.cfg

        self.assertFalse(
            elastic_db_repo.run_program(self.args, self.func_names))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_func_call_one(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_one

        Description:  Test run_program function with one call to function.

        Arguments:

        """

        self.args.args_array["-U"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.elr
        mock_load.return_value = self.cfg

        self.assertFalse(
            elastic_db_repo.run_program(self.args, self.func_names))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_func_call_zero(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_zero

        Description:  Test run_program function with zero calls to function.

        Arguments:

        """

        mock_lock.return_value = self.proglock
        mock_class.return_value = self.elr
        mock_load.return_value = self.cfg

        self.assertFalse(
            elastic_db_repo.run_program(self.args, self.func_names))


if __name__ == "__main__":
    unittest.main()
