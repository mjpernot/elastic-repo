#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
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
        els -> Stub argument holder.

    """

    status = True

    if els and dict(kwargs.get("args_array")):
        status = True

    return status


def list_repos(els, **kwargs):

    """Function:  list_repos

    Description:  This is a function stub for elastic_db_repo.list_repos.

    Arguments:
        els -> Stub argument holder.

    """

    status = True

    if els and dict(kwargs.get("args_array")):
        status = True

    return status


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            (input) cmdline -> Argv command line.
            (input) flavor -> Lock flavor ID.

        """

        self.cmdline = cmdline
        self.flavor = flavor


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_programlock_id -> Test ProgramLock with flavor ID.
        test_exception_handler -> Test with exception handler.
        test_func_call_multi -> Test run_program with multiple calls.
        test_func_call_one -> Test run_program with one call to function.
        test_func_call_zero -> Test run_program with zero calls to function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CfgTest(object):

            """Class:  CfgTest

            Description:  Class which is a representation of a cfg module.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.host = ["SERVER_NAME"]
                self.port = 9200

        self.cfg = CfgTest()

        self.args = {"-c": "config_file", "-d": "config_dir", "-M": True}
        self.func_dict = {"-U": disk_usage, "-R": list_repos}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_programlock_id(self, mock_lock, mock_class, mock_load):

        """Function:  test_programlock_id

        Description:  Test ProgramLock with flavor ID.

        Arguments:

        """

        self.args["-U"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = "Elastic_Class"
        mock_load.return_value = self.cfg

        self.assertFalse(elastic_db_repo.run_program(self.args,
                                                     self.func_dict))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_exception_handler(self, mock_lock, mock_class, mock_load):

        """Function:  test_exception_handler

        Description:  Test with exception handler.

        Arguments:

        """

        self.args["-U"] = True

        mock_lock.side_effect = \
            elastic_db_repo.gen_class.SingleInstanceException
        mock_class.return_value = "Elastic_Class"
        mock_load.return_value = self.cfg

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.run_program(self.args,
                                                         self.func_dict))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_func_call_multi(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_multi

        Description:  Test run_program function with multiple calls to
            function.

        Arguments:

        """

        self.args["-U"] = True
        self.args["-R"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = "Elastic_Class"
        mock_load.return_value = self.cfg

        self.assertFalse(elastic_db_repo.run_program(self.args,
                                                     self.func_dict))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_func_call_one(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_one

        Description:  Test run_program function with one call to function.

        Arguments:

        """

        self.args["-U"] = True

        mock_lock.return_value = self.proglock
        mock_class.return_value = "Elastic_Class"
        mock_load.return_value = self.cfg

        self.assertFalse(elastic_db_repo.run_program(self.args,
                                                     self.func_dict))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class.ProgramLock")
    def test_func_call_zero(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_zero

        Description:  Test run_program function with zero calls to function.

        Arguments:

        """

        mock_lock.return_value = self.proglock
        mock_class.return_value = "Elastic_Class"
        mock_load.return_value = self.cfg

        self.assertFalse(elastic_db_repo.run_program(self.args,
                                                     self.func_dict))


if __name__ == "__main__":
    unittest.main()
