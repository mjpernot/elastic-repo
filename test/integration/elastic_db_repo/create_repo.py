# Classification (U)

"""Program:  create_repo.py

    Description:  Integration testing of create_repo in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/create_repo.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_db_repo                          # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import elastic_lib.elastic_class as els     # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

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

        self.args_array = {}

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
        test_createrepo_cmdline
        test_createrepo_arg
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
        self.repo_name = "TEST_INTR_REPO"
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.user = self.cfg.user if hasattr(self.cfg, "user") else None
        self.japd = self.cfg.japd if hasattr(self.cfg, "japd") else None
        self.ca_cert = self.cfg.ssl_client_ca if hasattr(
            self.cfg, "ssl_client_ca") else None
        self.els = els.ElasticSearchRepo(
            self.cfg.host, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert)
        self.els.connect()

        if self.els.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_createrepo_cmdline(self):

        """Function:  test_createrepo_cmdline

        Description:  Test creating repository from command line.

        Arguments:

        """

        self.args.args_array = {
            "-C": self.repo_name, "-l": self.cfg.log_repo_dir}

        self.assertFalse(elastic_db_repo.create_repo(self.els, args=self.args))

    def test_createrepo_arg(self):

        """Function:  test_createrepo_arg

        Description:  Test creating repository from argument list.

        Arguments:

        """

        self.assertFalse(
            elastic_db_repo.create_repo(
                self.els, repo_name=self.repo_name,
                repo_dir=self.cfg.log_repo_dir, args=self.args))

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        err_flag, msg = self.els.delete_repo(self.repo_name)

        if err_flag:
            print(f"Error: Failed to remove repository {self.repo_name}")
            print(f"Reason: {msg}")

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
