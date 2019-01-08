#!/usr/bin/python
# Classification (U)

"""Program:  rename_repo.py

    Description:  Integration testing of rename_repo in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/rename_repo.py

    Arguments:
        None

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

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Integration testing initilization.
        test_renamerepo_cmdline -> Test rename repository from command line.
        test_renamerepo_arg -> Test rename repository from argument list.
        tearDown -> Clean up of integration testing.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.base_dir = "test/integration/elastic_db_repo"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("elastic", self.config_path)

        self.repo_name = "TEST_INTR_REPO"
        self.repo_name2 = "TEST_INTR_REPO2"
        self.repo_dir = os.path.join(self.cfg.base_repo_dir, self.repo_name)

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)

        if self.ER.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

        else:
            _, _ = self.ER.create_repo(repo_name=self.repo_name,
                                       repo_dir=self.repo_dir)

    def test_renamerepo_cmdline(self):

        """Function:  test_renamerepo_cmdline

        Description:  Test rename repository from command line.

        Arguments:
            None

        """

        args_array = {"-M": [self.repo_name, self.repo_name2]}

        self.assertFalse(elastic_db_repo.rename_repo(self.ER,
                                                     args_array=args_array))

    def test_renamerepo_arg(self):

        """Function:  test_renamerepo_arg

        Description:  Test rename repository from argument list.

        Arguments:
            None

        """

        self.assertFalse(elastic_db_repo.rename_repo(
            self.ER, name_list=[self.repo_name, self.repo_name2]))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:
            None

        """

        err_flag, msg = self.ER.delete_repo(self.repo_name2)

        if err_flag:
            print("Error: Failed to remove repository '%s'"
                  % self.repo_name)
            print("Reason: '%s'" % (msg))

        if os.path.isdir(self.repo_dir):
            shutil.rmtree(self.repo_dir)


if __name__ == "__main__":
    unittest.main()
