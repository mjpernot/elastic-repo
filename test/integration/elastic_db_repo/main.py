#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Integration testing of main in elastic_db_repo.py.

    Usage:
        test/integration/elastic_db_repo/main.py

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
import mock

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
        setUp -> Unit testing initilization.
        test_delete_dump -> Test delete dump call.
        test_rename_repo -> Test rename repo call.
        test_delete_repo -> Test delete repo call.
        test_disk_usage -> Test disk usage call.
        test_list_repos -> Test list repos call.
        test_list_dumps -> Test list dumps call.
        test_create_repo -> Test create repo call.
        test_arg_dir_chk_crt -> Test arg dir chk crt call.
        test_arg_cond_req_or -> Test arg cond req or call.
        test_arg_xor_dict -> Test arg xor dict call.
        test_arg_require -> Test arg require call.
        test_help_func -> Test help call.
        tearDown -> Unit testing cleanup.

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

        self.argv_list = [os.path.join(self.base_dir, "main.py"),
                          "-c", "elastic", "-d", self.config_path]

        self.repo_name = "TEST_INTR_REPO"
        self.repo_name2 = "TEST_INTR_REPO2"
        self.dump_name = "test_dump"
        self.repo_dir = os.path.join(self.cfg.base_repo_dir, self.repo_name)

        self.ER = None

        ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)

        if ER.repo_dict:
            print("ERROR: Test environment not clean - repositories exist.")
            self.skipTest("Pre-conditions not met.")

    def test_delete_dump(self):

        """Function:  test_delete_dump

        Description:  Test delete dump call.

        Arguments:
            None

        """

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)

        status, msg = self.ER.create_repo(self.repo_name, self.repo_dir)

        if status:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (msg))
            self.skipTest("Pre-conditions not met.")

        ES = elastic_class.ElasticSearchDump(self.cfg.host,
                                             repo=self.repo_name)
        ES.dump_name = self.dump_name
        status, msg = ES.dump_db()

        if status:
            print("Error detected for dump in repository: %s"
                  % (self.repo_name))
            print("Reason: %s" % (msg))
            self.skipTest("Dump failed")

        self.argv_list.append("-S")
        self.argv_list.append(self.dump_name)
        self.argv_list.append("-r")
        self.argv_list.append(self.repo_name)
        sys.argv = self.argv_list

        elastic_db_repo.main()

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port,
                                                  repo=self.repo_name)

        if self.dump_name not in elastic_class.get_dump_list(self.ER.es,
                                                             self.repo_name):
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_rename_repo(self):

        """Function:  test_rename_repo

        Description:  Test rename repo call.

        Arguments:
            None

        """

        self.argv_list.append("-M")
        self.argv_list.append(self.repo_name2)
        self.argv_list.append(self.repo_name)
        sys.argv = self.argv_list

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)

        status, msg = self.ER.create_repo(self.repo_name2, self.repo_dir)

        if status:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (msg))
            self.skipTest("Pre-conditions not met.")

        elastic_db_repo.main()

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port,
                                                  repo=self.repo_name)

        if self.repo_name in self.ER.repo_dict:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_delete_repo(self):

        """Function:  test_delete_repo

        Description:  Test delete repo call.

        Arguments:
            None

        """

        self.argv_list.append("-D")
        self.argv_list.append(self.repo_name)
        sys.argv = self.argv_list

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)

        status, msg = self.ER.create_repo(self.repo_name, self.repo_dir)

        if status:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (msg))
            self.skipTest("Pre-conditions not met.")

        elastic_db_repo.main()

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port,
                                                  repo=self.repo_name)

        if self.repo_name not in self.ER.repo_dict:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_disk_usage(self):

        """Function:  test_disk_usage

        Description:  Test disk usage call.

        Arguments:
            None

        """

        self.argv_list.append("-U")
        sys.argv = self.argv_list

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)

        status, msg = self.ER.create_repo(self.repo_name, self.repo_dir)

        if status:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (msg))
            self.skipTest("Pre-conditions not met.")

        # Wait until the repo dir has been created.
        while True:
            if not os.path.isdir(self.repo_dir):
                time.sleep(1)

            else:
                break

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_list_repos(self):

        """Function:  test_list_repos

        Description:  Test list repos call.

        Arguments:
            None

        """

        self.argv_list.append("-R")
        sys.argv = self.argv_list

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)

        status, msg = self.ER.create_repo(self.repo_name, self.repo_dir)

        if status:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (msg))
            self.skipTest("Pre-conditions not met.")

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_list_dumps(self):

        """Function:  test_list_dumps

        Description:  Test list dumps call.

        Arguments:
            None

        """

        self.argv_list.append("-L")
        self.argv_list.append(self.repo_name)
        sys.argv = self.argv_list

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port)

        status, msg = self.ER.create_repo(self.repo_name, self.repo_dir)

        if status:
            print("ERROR: Test repo failed to be created.")
            print("Reason:  %s" % (msg))
            self.skipTest("Pre-conditions not met.")

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_create_repo(self):

        """Function:  test_create_repo

        Description:  Test create repo call.

        Arguments:
            None

        """

        self.argv_list.append("-C")
        self.argv_list.append(self.repo_name)
        self.argv_list.append("-l")
        self.argv_list.append(self.repo_dir)
        sys.argv = self.argv_list

        elastic_db_repo.main()

        self.ER = elastic_class.ElasticSearchRepo(self.cfg.host, self.cfg.port,
                                                  repo=self.repo_name)

        if self.repo_name in self.ER.repo_dict:
            status = True

        else:
            status = False

        self.assertTrue(status)

    def test_arg_dir_chk_crt(self):

        """Function:  test_arg_dir_chk_crt

        Description:  Test arg dir chk crt call.

        Arguments:
            None

        """
        self.argv_list.remove(self.config_path)
        self.argv_list.append("TEST_DIR")
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_arg_cond_req_or(self):

        """Function:  test_arg_cond_req_or

        Description:  Test arg cond req or call.

        Arguments:
            None

        """

        self.argv_list.append("-C")
        self.argv_list.append(self.repo_name)
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_arg_xor_dict(self):

        """Function:  test_arg_xor_dict

        Description:  Test arg xor dict call.

        Arguments:
            None

        """

        self.argv_list.append("-U")
        self.argv_list.append("-D")
        self.argv_list.append(self.repo_name)
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_arg_require(self):

        """Function:  test_arg_require

        Description:  Test arg require call.

        Arguments:
            None

        """

        self.argv_list.remove("-c")
        self.argv_list.remove("elastic")
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def test_help_func(self):

        """Function:  test_help_func

        Description:  Test help call.

        Arguments:
            None

        """

        self.argv_list.append("-v")
        sys.argv = self.argv_list

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.main())

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of integration testing.

        Arguments:
            None

        """

        if self.ER and ("-C" in self.argv_list or "-L" in self.argv_list or
                        "-R" in self.argv_list or "-U" in self.argv_list or
                        "-M" in self.argv_list):

            status, msg = self.ER.delete_repo(self.repo_name)

            if status:
                print("Error: Failed to remove repository '%s'"
                      % self.repo_name)
                print("Reason: '%s'" % (msg))

            if os.path.isdir(self.repo_dir):
                os.rmdir(self.repo_dir)

        elif self.ER and "-S" in self.argv_list:

            status, msg = self.ER.delete_repo(self.repo_name)

            if status:
                print("Error: Failed to remove repository '%s'"
                      % self.repo_name)
                print("Reason: '%s'" % (msg))

            if os.path.isdir(self.repo_dir):
                shutil.rmtree(self.repo_dir)


if __name__ == "__main__":
    unittest.main()
