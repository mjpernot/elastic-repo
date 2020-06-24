#!/usr/bin/python
# Classification (U)

"""Program:  delete_repo.py

    Description:  Integration testing of delete_repo in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/delete_repo.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import elastic_db_repo
import lib.gen_libs as gen_libs
import elastic_lib.elastic_class as elastic_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Integration testing initilization.
        test_deleterepo_cmdline -> Test deleting repository from command line.
        test_deleterepo_arg -> Test deleting repository from argument list.
        tearDown -> Clean up of integration testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration/elastic_db_repo"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("elastic", self.config_path)
        self.repo_name = "TEST_INTR_REPO"
        self.repo_dir = os.path.join(self.cfg.log_repo_dir, self.repo_name)
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.els = elastic_class.ElasticSearchRepo(self.cfg.host,
                                                   self.cfg.port)

        if self.els.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

        else:
            _, _ = self.els.create_repo(repo_name=self.repo_name,
                                        repo_dir=self.repo_dir)

    def test_deleterepo_cmdline(self):

        """Function:  test_deleterepo_cmdline

        Description:  Test deleting repository from command line.

        Arguments:

        """

        args_array = {"-D": "TEST_INTR_REPO"}

        self.assertFalse(elastic_db_repo.delete_repo(self.els,
                                                     args_array=args_array))

    def test_deleterepo_arg(self):

        """Function:  test_deleterepo_arg

        Description:  Test deleting repository from argument list.

        Arguments:

        """

        self.assertFalse(elastic_db_repo.delete_repo(
            self.els, repo_name=self.repo_name, args_array={}))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
