# Classification (U)

"""Program:  delete_dump.py

    Description:  Integration testing of delete_dump in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/delete_dump.py

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


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = dict()

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_deletedmp_cmdline
        test_deletedmp_arg
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.base_dir = "test/integration/elastic_db_repo"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("elastic", self.config_path)
        self.dump_name = "test_dump"
        self.repo_name = "TEST_INTR_REPO"
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.user = self.cfg.user if hasattr(self.cfg, "user") else None
        self.japd = self.cfg.japd if hasattr(self.cfg, "japd") else None
        self.ca_cert = self.cfg.ssl_client_ca if hasattr(
            self.cfg, "ssl_client_ca") else None
        self.scheme = self.cfg.scheme if hasattr(
            self.cfg, "scheme") else "https"
        self.elr = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.elr.connect()

        if self.elr.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

        else:
            _, _ = self.elr.create_repo(
                repo_name=self.repo_name, repo_dir=self.cfg.log_repo_dir)

            self.els = elastic_class.ElasticSearchDump(
                self.cfg.host, port=self.cfg.port, repo=self.repo_name,
                user=self.user, japd=self.japd, ca_cert=self.ca_cert,
                scheme=self.scheme)
            self.els.connect()
            self.els.dump_name = self.dump_name
            self.els.dump_db()

    def test_deletedmp_cmdline(self):

        """Function:  test_deletedmp_cmdline

        Description:  Test delete dump from command line.

        Arguments:

        """

        self.args.args_array = {"-r": self.repo_name, "-S": self.dump_name}

        self.assertFalse(elastic_db_repo.delete_dump(self.elr, args=self.args))

    def test_deletedmp_arg(self):

        """Function:  test_deletedmp_arg

        Description:  Test delete dump from argument list.

        Arguments:

        """

        self.assertFalse(
            elastic_db_repo.delete_dump(
                self.elr, repo_name=self.repo_name, dump_name=self.dump_name,
                args=self.args))

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
