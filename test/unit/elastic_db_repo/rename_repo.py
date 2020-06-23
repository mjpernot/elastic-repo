#!/usr/bin/python
# Classification (U)

"""Program:  rename_repo.py

    Description:  Unit testing of rename_repo in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/rename_repo.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import elastic_db_repo
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_no_argsarray_is_passed -> Test when args_array is not passed.
        test_namelist_delete_err_false -> Test delete error flag of false.
        test_namelist_delete_err_true -> Test delete error flag of true.
        test_namelist_create_err_false -> Test create repo error flag of false.
        test_namelist_create_err_true -> Test create repo error flag of true.
        test_namelist_arg2_does_exist -> Test name arg 2 repo does exist.
        test_namelist_arg1_not_exist -> Test name arg 1 repo not exist.
        test_namelist_is_equal -> Test name list arg 1 and arg 2 are equal.
        test_namelist_is_not_list -> Test name list is not a list.
        test_namelist_is_not_len_two -> Test name list is not a length of two.
        test_namelist_is_passed -> Test name list is passed as argument.
        test_namelist_not_passed -> Test name list is not passed as argument.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class ElasticSearchRepo(object):

            """Class:  ElasticSearchRepo

            Description:  Class representation of the ElasticSearchRepo class.

            Methods:
                __init__ -> Initialize configuration environment.
                create_repo -> Mock of creating a repository.
                delete_repo -> Mock of deleting a repository.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the class.

                Arguments:

                """

                self.repo_dict = {
                    "Test_Repo_Name_1": {
                        "type": "fs", "settings": {
                            "compress": "true",
                            "location": "/dir/TEST_REPO1"}},
                    "Test_Repo_Name_2": {
                        "type": "fs", "settings": {
                            "compress": "true",
                            "location": "/dir/TEST_REPO2"}}}
                self.repo_dir = None

            def create_repo(self, repo_name, repo_dir):

                """Method:  create_repo

                Description:  Mock of creating a repository.

                Arguments:
                    (input) repo -> Name of repository.
                    (input) repo_dir -> Directory path to respository.
                    (output) err_flag -> True | False - Error status.
                    (output) status_msg -> Status error message or None.

                """

                self.repo_dir = repo_dir
                err_flag = False
                err_msg = None

                if repo_name == "Test_Repo_Name_F":
                    err_flag = True
                    err_msg = "Error_Message_Here1"

                return err_flag, err_msg

            def delete_repo(self, repo_name):

                """Method:  delete_repo

                Description:  Mock of deleting a repository.

                Arguments:
                    (input) repo -> Name of repository.
                    (output) err_flag -> True | False - Error status.
                    (output) status_msg -> Status error message or None.

                """

                err_flag = False
                err_msg = None

                if repo_name == "Test_Repo_Name_2":
                    err_flag = True
                    err_msg = "Error_Message_Here2"

                return err_flag, err_msg

        self.els = ElasticSearchRepo()

        self.args_array = {"-M": ["Test_Repo_Name_1", "Test_Dump_Name_5"]}

    @unittest.skip("Known Bug: Requires the args_array to be passed.")
    def test_no_argsarray_is_passed(self):

        """Function:  test_no_argsarray_is_passed

        Description:  Test when args_array is not passed to function.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, name_list=["Test_Repo_Name_1"]))

    def test_namelist_delete_err_false(self):

        """Function:  test_namelist_delete_err_false

        Description:  Test delete repo returns error flag of false.

        Arguments:

        """

        self.assertFalse(elastic_db_repo.rename_repo(
            self.els, args_array=self.args_array))

    def test_namelist_delete_err_true(self):

        """Function:  test_namelist_delete_err_true

        Description:  Test delete repo returns error flag of true.

        Arguments:

        """

        self.args_array = {"-M": ["Test_Repo_Name_2", "Test_Repo_Name_5"]}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, args_array=self.args_array))

    def test_namelist_create_err_false(self):

        """Function:  test_namelist_create_err_false

        Description:  Test create repo returns error flag of false.

        Arguments:

        """

        self.args_array = {"-M": ["Test_Repo_Name_1", "Test_Repo_Name_5"]}

        self.assertFalse(elastic_db_repo.rename_repo(
            self.els, args_array=self.args_array))

    def test_namelist_create_err_true(self):

        """Function:  test_namelist_create_err_true

        Description:  Test create repo returns error flag of true.

        Arguments:

        """

        self.args_array = {"-M": ["Test_Repo_Name_1", "Test_Repo_Name_F"]}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, args_array=self.args_array))

    def test_namelist_arg2_does_exist(self):

        """Function:  test_namelist_arg2_does_exist

        Description:  Test name arg 2 repo does exist.

        Arguments:

        """

        self.args_array = {"-M": ["Test_Repo_Name_1", "Test_Repo_Name_2"]}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, args_array=self.args_array))

    def test_namelist_arg1_not_exist(self):

        """Function:  test_namelist_arg1_not_exist

        Description:  Test name arg 1 repo not exist.

        Arguments:

        """

        self.args_array = {"-M": ["Test_Repo_Name_5", "Test_Repo_Name_6"]}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, args_array=self.args_array))

    def test_namelist_is_equal(self):

        """Function:  test_namelist_is_equal

        Description:  Test name list arg 1 and arg 2 are equal.

        Arguments:

        """

        self.args_array = {"-M": ["Test_Repo_Name_1", "Test_Repo_Name_1"]}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, args_array=self.args_array))

    def test_namelist_is_not_list(self):

        """Function:  test_namelist_is_not_list

        Description:  Test name list is not a list.

        Arguments:

        """

        self.args_array = {"-M": ("Test_Repo_Name_1", "Test_Repo_Name_5")}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, args_array=self.args_array))

    def test_namelist_is_not_len_two(self):

        """Function:  test_namelist_is_not_len_two

        Description:  Test name list is not a length of two.

        Arguments:

        """

        self.args_array["-M"] = ["Test_Repo_Name_1"]

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, args_array=self.args_array))

    def test_namelist_is_passed(self):

        """Function:  test_namelist_is_passed

        Description:  Test name list is passed as an argument.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, name_list=["Test_Repo_Name_1"], args_array={}))

    def test_namelist_not_passed(self):

        """Function:  test_namelist_not_passed

        Description:  Test name list is not passed as an argument.

        Arguments:

        """

        self.args_array["-M"] = ["Test_Repo_Name_1"]

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.rename_repo(
                self.els, args_array=self.args_array))


if __name__ == "__main__":
    unittest.main()
