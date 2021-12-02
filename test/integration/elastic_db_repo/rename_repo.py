#!/usr/bin/python
# Classification (U)

"""Program:  rename_repo.py

    Description:  Integration testing of rename_repo in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/rename_repo.py

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
        test_renamerepo_cmdline -> Test rename repository from command line.
        test_renamerepo_arg -> Test rename repository from argument list.
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
        self.repo_name2 = "TEST_INTR_REPO2"
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.user = cfg.user if hasattr(self.cfg, "user") else None
        self.japd = cfg.japd if hasattr(self.cfg, "japd") else None
        self.ca_cert = cfg.ssl_client_ca if hasattr(
            self.cfg, "ssl_client_ca") else None
        self.scheme = cfg.scheme if hasattr(self.cfg, "scheme") else "https"
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()

        if self.els.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

        else:
            _, _ = self.els.create_repo(repo_name=self.repo_name,
                                        repo_dir=self.cfg.log_repo_dir)

    def test_renamerepo_cmdline(self):

        """Function:  test_renamerepo_cmdline

        Description:  Test rename repository from command line.

        Arguments:

        """

        args_array = {"-M": [self.repo_name, self.repo_name2]}

        self.assertFalse(elastic_db_repo.rename_repo(self.els,
                                                     args_array=args_array))

    def test_renamerepo_arg(self):

        """Function:  test_renamerepo_arg

        Description:  Test rename repository from argument list.

        Arguments:

        """

        self.assertFalse(elastic_db_repo.rename_repo(
            self.els, name_list=[self.repo_name, self.repo_name2],
            args_array={}))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        err_flag, msg = self.els.delete_repo(self.repo_name2)

        if err_flag:
            print("Error: Failed to remove repository '%s'"
                  % self.repo_name)
            print("Reason: '%s'" % (msg))

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
