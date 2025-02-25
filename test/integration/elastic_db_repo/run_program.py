# Classification (U)

"""Program:  run_program.py

    Description:  Integration testing of run_program in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/run_program.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import shutil
import time
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_db_repo                          # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import elastic_lib.elastic_class as elcs    # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__

# Global


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_delete_dump
        test_list_dumps
        test_disk_usage
        test_rename_repo
        test_list_repos
        test_delete_repo
        test_create_repo
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
        self.repo_name2 = "TEST_INTR_REPO2"
        self.dump_name = "test_dump"
        self.phy_repo_dir = os.path.join(self.cfg.phy_repo_dir, self.repo_name)
        self.func_names = {
            "-L": elastic_db_repo.list_dumps,
            "-R": elastic_db_repo.list_repos,
            "-C": elastic_db_repo.create_repo,
            "-D": elastic_db_repo.delete_repo,
            "-S": elastic_db_repo.delete_dump,
            "-M": elastic_db_repo.rename_repo,
            "-U": elastic_db_repo.disk_usage}
        self.args = {"-c": "elastic", "-d": self.config_path}
        self.user = self.cfg.user if hasattr(self.cfg, "user") else None
        self.japd = self.cfg.japd if hasattr(self.cfg, "japd") else None
        self.ca_cert = self.cfg.ssl_client_ca if hasattr(
            self.cfg, "ssl_client_ca") else None
        self.scheme = self.cfg.scheme if hasattr(
            self.cfg, "scheme") else "https"
        self.els = elcs.ElasticSearchRepo(
            self.cfg.host, port=self.cfg.port, user=self.user, japd=self.japd,
            ca_cert=self.ca_cert, scheme=self.scheme)
        self.els.connect()
        self.els2 = None

        if self.els.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_delete_dump(self):

        """Function:  test_delete_dump

        Description:  Test delete dump call.

        Arguments:

        """

        err_flag, status_msg = self.els.create_repo(
            self.repo_name, self.cfg.log_repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print(f"Reason:  {status_msg}")
            self.skipTest("Pre-conditions not met.")

        els2 = elcs.ElasticSearchDump(
            self.cfg.host, port=self.cfg.port, repo=self.repo_name,
            user=self.user, japd=self.japd, ca_cert=self.ca_cert,
            scheme=self.scheme)
        els2.connect()
        els2.dump_name = self.dump_name
        err_flag, msg = els2.dump_db()

        if err_flag:
            print(f"Error detected for dump in repository: {self.repo_name}")
            print(f"Reason: {msg}")
            self.skipTest("Dump failed")

        self.args["-S"] = self.dump_name
        self.args["-r"] = self.repo_name

        self.assertFalse(elastic_db_repo.run_program(
            self.args, self.func_names))

    def test_list_dumps(self):

        """Function:  test_list_dumps

        Description:  Test list dumps call.

        Arguments:

        """

        err_flag, status_msg = self.els.create_repo(
            self.repo_name, self.cfg.log_repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print(f"Reason:  {status_msg}")
            self.skipTest("Pre-conditions not met.")

        els2 = elcs.ElasticSearchDump(
            self.cfg.host, port=self.cfg.port, repo=self.repo_name,
            user=self.user, japd=self.japd, ca_cert=self.ca_cert,
            scheme=self.scheme)
        els2.connect()
        err_flag, msg = els2.dump_db()

        if err_flag:
            print(f"Error detected for dump in repository: {self.repo_name}")
            print(f"Reason: {msg}")
            self.skipTest("Dump failed")

        self.args["-L"] = self.repo_name

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.run_program(self.args, self.func_names))

    @unittest.skip("Error:  Fails in a docker setup environment.")
    def test_disk_usage(self):

        """Function:  test_disk_usage

        Description:  Test disk usage call.

        Arguments:

        """

        err_flag, status_msg = self.els.create_repo(
            self.repo_name, self.cfg.log_repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print(f"Reason:  {status_msg}")
            self.skipTest("Pre-conditions not met.")

        # Wait until the repo dir has been created.
        while True:
            if not os.path.isdir(self.phy_repo_dir):
                time.sleep(1)

            else:
                break

        self.args["-U"] = True

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.run_program(self.args, self.func_names))

    def test_rename_repo(self):

        """Function:  test_rename_repo

        Description:  Test rename repo call.

        Arguments:

        """

        err_flag, status_msg = self.els.create_repo(
            self.repo_name, self.cfg.log_repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print(f"Reason:  {status_msg}")
            self.skipTest("Pre-conditions not met.")

        self.args["-M"] = [self.repo_name, self.repo_name2]

        elastic_db_repo.run_program(self.args, self.func_names)

        self.els2 = elcs.ElasticSearchRepo(
            self.cfg.host, self.cfg.port, repo=self.repo_name2, user=self.user,
            japd=self.japd, ca_cert=self.ca_cert, scheme=self.scheme)
        self.els2.connect()

        self.assertIn(self.repo_name2, self.els2.repo_dict)

    def test_list_repos(self):

        """Function:  test_list_repos

        Description:  Test list repos call.

        Arguments:

        """

        err_flag, status_msg = self.els.create_repo(
            self.repo_name, self.cfg.log_repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print(f"Reason:  {status_msg}")
            self.skipTest("Pre-conditions not met.")

        self.args["-R"] = True

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.run_program(self.args, self.func_names))

    def test_delete_repo(self):

        """Function:  test_delete_repo

        Description:  Test delete repo call.

        Arguments:

        """

        err_flag, status_msg = self.els.create_repo(
            self.repo_name, self.cfg.log_repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print(f"Reason:  {status_msg}")
            self.skipTest("Pre-conditions not met.")

        self.args["-D"] = self.repo_name

        elastic_db_repo.run_program(self.args, self.func_names)

        self.els2 = elcs.ElasticSearchRepo(
            self.cfg.host, self.cfg.port, repo=self.repo_name, user=self.user,
            japd=self.japd, ca_cert=self.ca_cert, scheme=self.scheme)
        self.els2.connect()

        self.assertNotIn(self.repo_name, self.els2.repo_dict)

    def test_create_repo(self):

        """Function:  test_create_repo

        Description:  Test create repo call.

        Arguments:

        """

        self.args["-C"] = self.repo_name
        self.args["-l"] = self.cfg.log_repo_dir

        elastic_db_repo.run_program(self.args, self.func_names)

        self.els2 = elcs.ElasticSearchRepo(
            self.cfg.host, self.cfg.port, repo=self.repo_name, user=self.user,
            japd=self.japd, ca_cert=self.ca_cert, scheme=self.scheme)
        self.els2.connect()

        self.assertIn(self.repo_name, self.els2.repo_dict)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if "-C" in self.args or "-R" in self.args or "-U" in self.args \
           or "-L" in self.args or "-S" in self.args:
            els = elcs.ElasticSearchRepo(
                self.cfg.host, port=self.cfg.port, user=self.user,
                japd=self.japd, ca_cert=self.ca_cert, scheme=self.scheme)
            els.connect()

            err_flag, status_msg = els.delete_repo(self.repo_name)

            if err_flag:
                print(f"Error: Failed to remove repository {self.repo_name}")
                print(f"Reason:  {status_msg}")

        elif "-M" in self.args:
            els = elcs.ElasticSearchRepo(
                self.cfg.host, port=self.cfg.port, user=self.user,
                japd=self.japd, ca_cert=self.ca_cert, scheme=self.scheme)
            els.connect()

            err_flag, status_msg = els.delete_repo(self.repo_name2)

            if err_flag:
                print(f"Error: Failed to remove repository {self.repo_name2}")
                print(f"Reason:  {status_msg}")

        if os.path.isdir(self.phy_repo_dir):
            shutil.rmtree(self.phy_repo_dir)


if __name__ == "__main__":
    unittest.main()
