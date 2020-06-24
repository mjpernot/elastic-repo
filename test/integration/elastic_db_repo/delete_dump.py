#!/usr/bin/python
# Classification (U)

"""Program:  delete_dump.py

    Description:  Integration testing of delete_dump in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/delete_dump.py

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
        test_deletedmp_cmdline -> Test delete dump from command line.
        test_deletedmp_arg -> Test delete dump from argument list.
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
        self.dump_name = "test_dump"
        self.repo_name = "TEST_INTR_REPO"
        self.repo_dir = os.path.join(self.cfg.log_repo_dir, self.repo_name)
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.elr = elastic_class.ElasticSearchRepo(self.cfg.host,
                                                   self.cfg.port)

        if self.elr.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

        else:
            _, _ = self.elr.create_repo(repo_name=self.repo_name,
                                        repo_dir=self.repo_dir)

            self.els = elastic_class.ElasticSearchDump(
                self.cfg.host, self.cfg.port, repo=self.repo_name)
            self.els.dump_name = self.dump_name
            self.els.dump_db()

    def test_deletedmp_cmdline(self):

        """Function:  test_deletedmp_cmdline

        Description:  Test delete dump from command line.

        Arguments:

        """

        args_array = {"-r": self.repo_name, "-S": self.dump_name}

        self.assertFalse(elastic_db_repo.delete_dump(self.elr,
                                                     args_array=args_array))

    def test_deletedmp_arg(self):

        """Function:  test_deletedmp_arg

        Description:  Test delete dump from argument list.

        Arguments:

        """

        self.assertFalse(elastic_db_repo.delete_dump(
            self.elr, repo_name=self.repo_name, dump_name=self.dump_name,
            args_array={}))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        err_flag, msg = self.elr.delete_repo(self.repo_name)

        if err_flag:
            print("Error: Failed to remove repository '%s'"
                  % self.repo_name)
            print("Reason: '%s'" % (msg))

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
