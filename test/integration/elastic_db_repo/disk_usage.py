#!/usr/bin/python
# Classification (U)

"""Program:  disk_usage.py

    Description:  Integration testing of disk_usage in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/disk_usage.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil
import time

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
        test_disk_usage -> Test displaying disk usage.
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
        self.repo_dir = os.path.join(self.cfg.base_repo_dir, self.repo_name)

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)

        if self.ER.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

        else:
            _, _ = self.ER.create_repo(repo_name=self.repo_name,
                                       repo_dir=self.repo_dir)

    def test_disk_usage(self):

        """Function:  test_disk_usage

        Description:  Test displaying disk usage.

        Arguments:
            None

        """

        # Wait until the repo dir has been created.
        while True:
            if not os.path.isdir(self.repo_dir):
                time.sleep(1)

            else:
                break

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.disk_usage(self.ER))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:
            None

        """

        err_flag, msg = self.ER.delete_repo(self.repo_name)

        if err_flag:
            print("Error: Failed to remove repository '%s'"
                  % self.repo_name)
            print("Reason: '%s'" % (msg))

        if os.path.isdir(self.repo_dir):
            shutil.rmtree(self.repo_dir)


if __name__ == "__main__":
    unittest.main()
