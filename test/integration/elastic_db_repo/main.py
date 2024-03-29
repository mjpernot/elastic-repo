# Classification (U)

"""Program:  main.py

    Description:  Integration testing of main in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/main.py

    Arguments:

"""

# Libraries and Global Variables
from __future__ import print_function

# Standard
import sys
import os
import shutil
import time
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_db_repo
import lib.gen_libs as gen_libs
import elastic_lib.elastic_class as elastic_class
import version

__version__ = version.__version__

# Global
SKIP_PRINT = "Pre-conditions not met."
PRT_TEMPLATE = "Reason:  %s"
ERROR_PRINT = "ERROR: Test repo failed to be created."


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_delete_dump
        test_rename_repo
        test_delete_repo
        test_disk_usage
        test_list_repos
        test_list_dumps
        test_create_repo
        test_arg_dir_chk_crt
        test_arg_cond_req_or
        test_arg_xor_dict
        test_arg_require
        test_help_func
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        global SKIP_PRINT

        self.base_dir = "test/integration/elastic_db_repo"
        self.test_path = os.path.join(os.getcwd(), self.base_dir)
        self.config_path = os.path.join(self.test_path, "config")
        self.cfg = gen_libs.load_module("elastic", self.config_path)
        self.argv_list = [os.path.join(self.base_dir, "main.py"),
                          "-c", "elastic", "-d", self.config_path]
        self.repo_name = "TEST_INTR_REPO"
        self.repo_name2 = "TEST_INTR_REPO2"
        self.dump_name = "test_dump"
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.els = None
        self.user = self.cfg.user if hasattr(self.cfg, "user") else None
        self.japd = self.cfg.japd if hasattr(self.cfg, "japd") else None
        self.ca_cert = self.cfg.ssl_client_ca if hasattr(
            self.cfg, "ssl_client_ca") else None
        self.scheme = self.cfg.scheme if hasattr(
            self.cfg, "scheme") else "https"
        els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        els.connect()

        if els.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest(SKIP_PRINT)

    def test_delete_dump(self):

        """Function:  test_delete_dump

        Description:  Test delete dump call.

        Arguments:

        """

        global SKIP_PRINT
        global PRT_TEMPLATE
        global ERROR_PRINT

        cmdline = gen_libs.get_inst(sys)
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()
        status, msg = self.els.create_repo(
            self.repo_name, self.cfg.log_repo_dir)

        if status:
            print(ERROR_PRINT)
            print(PRT_TEMPLATE % (msg))
            self.skipTest(SKIP_PRINT)

        els = elastic_class.ElasticSearchDump(
            self.cfg.host, port=self.cfg.port, repo=self.repo_name,
            user=self.user, japd=self.japd, ca_cert=self.ca_cert,
            scheme=self.scheme)
        els.connect()
        els.dump_name = self.dump_name
        status, msg = els.dump_db()

        if status:
            print("Error detected for dump in repository: %s"
                  % (self.repo_name))
            print(PRT_TEMPLATE % (msg))
            self.skipTest("Dump failed")

        self.argv_list.append("-S")
        self.argv_list.append(self.dump_name)
        self.argv_list.append("-r")
        self.argv_list.append(self.repo_name)
        cmdline.argv = self.argv_list
        elastic_db_repo.main()
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, repo=self.repo_name,
            user=self.user, japd=self.japd, ca_cert=self.ca_cert,
            scheme=self.scheme)
        self.els.connect()

        self.assertTrue(
            True if self.dump_name not in elastic_class.get_dump_list(
                self.els.els, self.repo_name) else False)

    def test_rename_repo(self):

        """Function:  test_rename_repo

        Description:  Test rename repo call.

        Arguments:

        """

        global SKIP_PRINT
        global PRT_TEMPLATE
        global ERROR_PRINT

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-M")
        self.argv_list.append(self.repo_name2)
        self.argv_list.append(self.repo_name)
        cmdline.argv = self.argv_list
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()
        status, msg = self.els.create_repo(
            self.repo_name2, self.cfg.log_repo_dir)

        if status:
            print(ERROR_PRINT)
            print(PRT_TEMPLATE % (msg))
            self.skipTest(SKIP_PRINT)

        elastic_db_repo.main()
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, repo=self.repo_name,
            user=self.user, japd=self.japd, ca_cert=self.ca_cert,
            scheme=self.scheme)
        self.els.connect()

        self.assertTrue(
            True if self.repo_name in self.els.repo_dict else False)

    def test_delete_repo(self):

        """Function:  test_delete_repo

        Description:  Test delete repo call.

        Arguments:

        """

        global SKIP_PRINT
        global PRT_TEMPLATE
        global ERROR_PRINT

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-D")
        self.argv_list.append(self.repo_name)
        cmdline.argv = self.argv_list
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()
        status, msg = self.els.create_repo(
            self.repo_name, self.cfg.log_repo_dir)

        if status:
            print(ERROR_PRINT)
            print(PRT_TEMPLATE % (msg))
            self.skipTest(SKIP_PRINT)

        elastic_db_repo.main()
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, repo=self.repo_name,
            user=self.user, japd=self.japd, ca_cert=self.ca_cert,
            scheme=self.scheme)
        self.els.connect()

        self.assertTrue(
            True if self.repo_name not in self.els.repo_dict else False)

    @unittest.skip("Error:  Fails in a docker setup environment.")
    def test_disk_usage(self):

        """Function:  test_disk_usage

        Description:  Test disk usage call.

        Arguments:

        """

        global SKIP_PRINT
        global PRT_TEMPLATE
        global ERROR_PRINT

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-U")
        cmdline.argv = self.argv_list
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()
        status, msg = self.els.create_repo(self.repo_name,
                                           self.cfg.log_repo_dir)

        if status:
            print(ERROR_PRINT)
            print(PRT_TEMPLATE % (msg))
            self.skipTest(SKIP_PRINT)

        # Wait until the repo dir has been created.
        while True:
            if not os.path.isdir(self.phy_repo_dir):
                time.sleep(1)

            else:
                break

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_list_repos(self):

        """Function:  test_list_repos

        Description:  Test list repos call.

        Arguments:

        """

        global SKIP_PRINT
        global PRT_TEMPLATE
        global ERROR_PRINT

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-R")
        cmdline.argv = self.argv_list
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()
        status, msg = self.els.create_repo(self.repo_name,
                                           self.cfg.log_repo_dir)

        if status:
            print(ERROR_PRINT)
            print(PRT_TEMPLATE % (msg))
            self.skipTest(SKIP_PRINT)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_list_dumps(self):

        """Function:  test_list_dumps

        Description:  Test list dumps call.

        Arguments:

        """

        global SKIP_PRINT
        global PRT_TEMPLATE
        global ERROR_PRINT

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-L")
        self.argv_list.append(self.repo_name)
        cmdline.argv = self.argv_list
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()
        status, msg = self.els.create_repo(self.repo_name,
                                           self.cfg.log_repo_dir)

        if status:
            print(ERROR_PRINT)
            print(PRT_TEMPLATE % (msg))
            self.skipTest(SKIP_PRINT)

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_create_repo(self):

        """Function:  test_create_repo

        Description:  Test create repo call.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-C")
        self.argv_list.append(self.repo_name)
        self.argv_list.append("-l")
        self.argv_list.append(self.cfg.log_repo_dir)
        cmdline.argv = self.argv_list
        elastic_db_repo.main()
        self.els = elastic_class.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, repo=self.repo_name,
            user=self.user, japd=self.japd, ca_cert=self.ca_cert,
            scheme=self.scheme)
        self.els.connect()

        self.assertTrue(
            True if self.repo_name in self.els.repo_dict else False)

    def test_arg_dir_chk_crt(self):

        """Function:  test_arg_dir_chk_crt

        Description:  Test arg dir chk crt call.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.remove(self.config_path)
        self.argv_list.append("TEST_DIR")
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_arg_cond_req_or(self):

        """Function:  test_arg_cond_req_or

        Description:  Test arg cond req or call.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-C")
        self.argv_list.append(self.repo_name)
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_arg_xor_dict(self):

        """Function:  test_arg_xor_dict

        Description:  Test arg xor dict call.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-U")
        self.argv_list.append("-D")
        self.argv_list.append(self.repo_name)
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_arg_require(self):

        """Function:  test_arg_require

        Description:  Test arg require call.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.remove("-c")
        self.argv_list.remove("elastic")
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_help_func(self):

        """Function:  test_help_func

        Description:  Test help call.

        Arguments:

        """

        cmdline = gen_libs.get_inst(sys)
        self.argv_list.append("-v")
        cmdline.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        global PRT_TEMPLATE

        if self.els and ("-C" in self.argv_list or "-L" in self.argv_list or
                         "-R" in self.argv_list or "-U" in self.argv_list or
                         "-M" in self.argv_list or "-S" in self.argv_list):

            status, msg = self.els.delete_repo(self.repo_name)

            if status:
                print("Error: Failed to remove repository '%s'"
                      % self.repo_name)
                print(PRT_TEMPLATE % (msg))

            if os.path.isdir(self.phy_repo_dir):
                shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
