# Classification (U)

"""Program:  list_dumps.py

    Description:  Integration testing of list_dumps in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/list_dumps.py

    Arguments:

"""

# Libraries and Global Variables
from __future__ import print_function

# Standard
import sys
import os
import shutil
import unittest

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
        setUp
        test_listdumps_none
        test_repo_dict
        test_repo_class_attr
        tearDown

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
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.user = self.cfg.user if hasattr(self.cfg, "user") else None
        self.japd = self.cfg.japd if hasattr(self.cfg, "japd") else None
        self.ca_cert = self.cfg.ssl_client_ca if hasattr(
            self.cfg, "ssl_client_ca") else None
        self.scheme = self.cfg.scheme if hasattr(
            self.cfg, "scheme") else "https"
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()

        if self.els.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

        else:
            _, _ = self.els.create_repo(self.repo_name, self.cfg.log_repo_dir)

    def test_listdumps_none(self):

        """Function:  test_listdumps_none

        Description:  Test listing dumps in empty repository.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.list_dumps(self.els))

    def test_repo_dict(self):

        """Function:  test_repo_dict

        Description:  Get dumps using pull from dictionary.

        Arguments:

        """

        els = elastic_class.ElasticSearchDump(
            self.cfg.host, port=self.cfg.port, repo=self.repo_name,
            user=self.user, japd=self.japd, ca_cert=self.ca_cert,
            scheme=self.scheme)
        els.connect()
        err_flag, msg = els.dump_db()

        if err_flag:
            print("Error detected for dump in repository: %s"
                  % (self.repo_name))
            print("Reason: %s" % (msg))
            self.skipTest("Dump failed")

        else:
            with gen_libs.no_std_out():
                self.assertFalse(elastic_db_repo.list_dumps(self.els))

    def test_repo_class_attr(self):

        """Function:  test_repo_class_attr

        Description:  Get dumps using class attribute.

        Arguments:

        """

        els = elastic_class.ElasticSearchDump(
            self.cfg.host, port=self.cfg.port, repo=self.repo_name,
            user=self.user, japd=self.japd, ca_cert=self.ca_cert,
            scheme=self.scheme)
        els.connect()
        err_flag, msg = els.dump_db()

        if err_flag:
            print("Error detected for dump in repository: %s"
                  % (self.repo_name))
            print("Reason: %s" % (msg))
            self.skipTest("Dump failed")

        else:
            self.els.repo = self.repo_name

            with gen_libs.no_std_out():
                self.assertFalse(elastic_db_repo.list_dumps(self.els))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        err_flag, msg = self.els.delete_repo(self.repo_name)

        if err_flag:
            print("Error: Failed to remove repository '%s'"
                  % self.repo_name)
            print("Reason: '%s'" % (msg))

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
