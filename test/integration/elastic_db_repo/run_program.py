#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

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
        setUp -> Unit testing initilization.
        test_delete_dump -> Test delete dump call.
        test_list_dumps -> Test list dumps call.
        test_disk_usage -> Test disk usage call.
        test_rename_repo -> Test rename repo call.
        test_list_repos -> Test list repos call.
        test_delete_repo -> Test delete repo call.
        test_create_repo -> Test create repo call.
        tearDown -> Unit testing cleanup.

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
        self.repo_dir = os.path.join(self.cfg.base_repo_dir, self.repo_name)

        self.func_dict = {"-L": elastic_db_repo.list_dumps,
                          "-R": elastic_db_repo.list_repos,
                          "-C": elastic_db_repo.create_repo,
                          "-D": elastic_db_repo.delete_repo,
                          "-S": elastic_db_repo.delete_dump,
                          "-M": elastic_db_repo.rename_repo,
                          "-U": elastic_db_repo.disk_usage}
        self.args = {"-c": "elastic", "-d": self.config_path}

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)
        self.ER2 = None

        if self.ER.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_delete_dump(self):

        """Function:  test_delete_dump

        Description:  Test delete dump call.

        Arguments:

        """

        err_flag, status_msg = self.ER.create_repo(self.repo_name,
                                                   self.repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (status_msg))
            self.skipTest("Pre-conditions not met.")

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)
        ES.dump_name = self.dump_name
        err_flag, msg = ES.dump_db()

        if err_flag:
            print("Error detected for dump in repository: %s"
                  % (self.repo_name))
            print("Reason: %s" % (msg))
            self.skipTest("Dump failed")

        self.args["-S"] = self.dump_name
        self.args["-r"] = self.repo_name

        self.assertFalse(elastic_db_repo.run_program(self.args,
                                                     self.func_dict))

    def test_list_dumps(self):

        """Function:  test_list_dumps

        Description:  Test list dumps call.

        Arguments:

        """

        err_flag, status_msg = self.ER.create_repo(self.repo_name,
                                                   self.repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (status_msg))
            self.skipTest("Pre-conditions not met.")

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)
        err_flag, msg = ES.dump_db()

        if err_flag:
            print("Error detected for dump in repository: %s"
                  % (self.repo_name))
            print("Reason: %s" % (msg))
            self.skipTest("Dump failed")

        self.args["-L"] = self.repo_name

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.run_program(self.args,
                                                         self.func_dict))

    def test_disk_usage(self):

        """Function:  test_disk_usage

        Description:  Test disk usage call.

        Arguments:

        """

        err_flag, status_msg = self.ER.create_repo(self.repo_name,
                                                   self.repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (status_msg))
            self.skipTest("Pre-conditions not met.")

        # Wait until the repo dir has been created.
        while True:
            if not os.path.isdir(self.repo_dir):
                time.sleep(1)

            else:
                break

        self.args["-U"] = True

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.run_program(self.args,
                                                         self.func_dict))

    def test_rename_repo(self):

        """Function:  test_rename_repo

        Description:  Test rename repo call.

        Arguments:

        """

        err_flag, status_msg = self.ER.create_repo(self.repo_name,
                                                   self.repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (status_msg))
            self.skipTest("Pre-conditions not met.")

        self.args["-M"] = [self.repo_name, self.repo_name2]

        elastic_db_repo.run_program(self.args, self.func_dict)

        self.ER2 = elastic_class.ElasticSearchRepo(self.cfg.host,
                                                   self.cfg.port,
                                                   repo=self.repo_name2)

        if self.repo_name2 in self.ER2.repo_dict:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_list_repos(self):

        """Function:  test_list_repos

        Description:  Test list repos call.

        Arguments:

        """

        err_flag, status_msg = self.ER.create_repo(self.repo_name,
                                                   self.repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (status_msg))
            self.skipTest("Pre-conditions not met.")

        self.args["-R"] = True

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.run_program(self.args,
                                                         self.func_dict))

    def test_delete_repo(self):

        """Function:  test_delete_repo

        Description:  Test delete repo call.

        Arguments:

        """

        err_flag, status_msg = self.ER.create_repo(self.repo_name,
                                                   self.repo_dir)

        if err_flag:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (status_msg))
            self.skipTest("Pre-conditions not met.")

        self.args["-D"] = self.repo_name

        elastic_db_repo.run_program(self.args, self.func_dict)

        self.ER2 = elastic_class.ElasticSearchRepo(self.cfg.host,
                                                   self.cfg.port,
                                                   repo=self.repo_name)

        if self.repo_name not in self.ER2.repo_dict:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_create_repo(self):

        """Function:  test_create_repo

        Description:  Test create repo call.

        Arguments:

        """

        self.args["-C"] = self.repo_name
        self.args["-l"] = self.repo_dir

        elastic_db_repo.run_program(self.args, self.func_dict)

        self.ER2 = elastic_class.ElasticSearchRepo(self.cfg.host,
                                                   self.cfg.port,
                                                   repo=self.repo_name)

        if self.repo_name in self.ER2.repo_dict:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:

        """

        if "-C" in self.args or "-R" in self.args or "-U" in self.args \
           or "-L" in self.args or "-S" in self.args:
            ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                                 self.cfg.port)

            err_flag, status_msg = ER.delete_repo(self.repo_name)

            if err_flag:
                print("Error: Failed to remove repository '%s'"
                      % (self.repo_name))
                print("Reason: '%s'" % (status_msg))

        elif "-M" in self.args:
            ER = elastic_class.ElasticSearchRepo(self.cfg.host,
                                                 self.cfg.port)

            err_flag, status_msg = ER.delete_repo(self.repo_name2)

            if err_flag:
                print("Error: Failed to remove repository '%s'"
                      % (self.repo_name2))
                print("Reason: '%s'" % (status_msg))

        if os.path.isdir(self.repo_dir):
            shutil.rmtree(self.repo_dir)


if __name__ == "__main__":
    unittest.main()
