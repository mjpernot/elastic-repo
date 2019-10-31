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


def disk_usage(er, **kwargs):

    """Function:  disk_usage

    Description:  This is a function stub for elastic_db_repo.disk_usage.

    Arguments:
        er -> Stub argument holder.

    """

    pass


def list_repos(er, **kwargs):

    """Function:  list_repos

    Description:  This is a function stub for elastic_db_repo.list_repos.

    Arguments:
        er -> Stub argument holder.

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
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

        self.ct = CfgTest()

        self.args = {"-c": "config_file", "-d": "config_dir", "-M": True}
        self.func_dict = {"-U": disk_usage, "-R": list_repos}

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class")
    def test_func_call_multi(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_multi

        Description:  Test run_program function with multiple calls to
            function.

        Arguments:

        """

        self.args["-U"] = True
        self.args["-R"] = True

        mock_lock.ProgramLock = elastic_db_repo.gen_class.ProgramLock
        mock_class.return_value = "Elastic_Class"
        mock_load.return_value = self.ct

        self.assertFalse(elastic_db_repo.run_program(self.args,
                                                     self.func_dict))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class")
    def test_func_call_one(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_one

        Description:  Test run_program function with one call to function.

        Arguments:

        """

        self.args["-U"] = True

        mock_lock.ProgramLock = elastic_db_repo.gen_class.ProgramLock
        mock_class.return_value = "Elastic_Class"
        mock_load.return_value = self.ct

        self.assertFalse(elastic_db_repo.run_program(self.args,
                                                     self.func_dict))

    @mock.patch("elastic_db_repo.gen_libs.load_module")
    @mock.patch("elastic_db_repo.elastic_class.ElasticSearchRepo")
    @mock.patch("elastic_db_repo.gen_class")
    def test_func_call_zero(self, mock_lock, mock_class, mock_load):

        """Function:  test_func_call_zero

        Description:  Test run_program function with zero calls to function.

        Arguments:

        """

        mock_lock.ProgramLock = elastic_db_repo.gen_class.ProgramLock
        mock_class.return_value = "Elastic_Class"
        mock_load.return_value = self.ct

        self.assertFalse(elastic_db_repo.run_program(self.args,
                                                     self.func_dict))


if __name__ == "__main__":
    unittest.main()
