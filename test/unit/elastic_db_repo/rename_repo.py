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
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_db_repo
import lib.gen_libs as gen_libs
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


class ElasticSearchRepo(object):

    """Class:  ElasticSearchRepo

    Description:  Class representation of the ElasticSearchRepo class.

    Methods:
        __init__
        create_repo
        delete_repo

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

        """

        err_flag = False
        err_msg = None

        if repo_name == "Test_Repo_Name_2":
            err_flag = True
            err_msg = "Error_Message_Here2"

        return err_flag, err_msg


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_namelist_delete_err_false
        test_namelist_delete_err_true
        test_namelist_create_err_false
        test_namelist_create_err_true
        test_namelist_arg2_does_exist
        test_namelist_arg1_not_exist
        test_namelist_is_equal
        test_namelist_is_not_list
        test_namelist_is_not_len_two
        test_namelist_is_passed
        test_namelist_not_passed

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearchRepo()
        self.args = ArgParser()
        self.args.args_array = {"-M": ["Test_Repo_Name_1", "Test_Dump_Name_5"]}

    def test_namelist_delete_err_false(self):

        """Function:  test_namelist_delete_err_false

        Description:  Test delete repo returns error flag of false.

        Arguments:

        """

        self.assertFalse(elastic_db_repo.rename_repo(self.els, args=self.args))

    def test_namelist_delete_err_true(self):

        """Function:  test_namelist_delete_err_true

        Description:  Test delete repo returns error flag of true.

        Arguments:

        """

        self.args.args_array = {"-M": ["Test_Repo_Name_2", "Test_Repo_Name_5"]}

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.rename_repo(self.els, args=self.args))

    def test_namelist_create_err_false(self):

        """Function:  test_namelist_create_err_false

        Description:  Test create repo returns error flag of false.

        Arguments:

        """

        self.args.args_array = {"-M": ["Test_Repo_Name_1", "Test_Repo_Name_5"]}

        self.assertFalse(elastic_db_repo.rename_repo(self.els, args=self.args))

    def test_namelist_create_err_true(self):

        """Function:  test_namelist_create_err_true

        Description:  Test create repo returns error flag of true.

        Arguments:

        """

        self.args.args_array = {"-M": ["Test_Repo_Name_1", "Test_Repo_Name_F"]}

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.rename_repo(self.els, args=self.args))

    def test_namelist_arg2_does_exist(self):

        """Function:  test_namelist_arg2_does_exist

        Description:  Test name arg 2 repo does exist.

        Arguments:

        """

        self.args.args_array = {"-M": ["Test_Repo_Name_1", "Test_Repo_Name_2"]}

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.rename_repo(self.els, args=self.args))

    def test_namelist_arg1_not_exist(self):

        """Function:  test_namelist_arg1_not_exist

        Description:  Test name arg 1 repo not exist.

        Arguments:

        """

        self.args.args_array = {"-M": ["Test_Repo_Name_5", "Test_Repo_Name_6"]}

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.rename_repo(self.els, args=self.args))

    def test_namelist_is_equal(self):

        """Function:  test_namelist_is_equal

        Description:  Test name list arg 1 and arg 2 are equal.

        Arguments:

        """

        self.args.args_array = {"-M": ["Test_Repo_Name_1", "Test_Repo_Name_1"]}

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.rename_repo(self.els, args=self.args))

    def test_namelist_is_not_list(self):

        """Function:  test_namelist_is_not_list

        Description:  Test name list is not a list.

        Arguments:

        """

        self.args.args_array = {"-M": ("Test_Repo_Name_1", "Test_Repo_Name_5")}

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.rename_repo(self.els, args=self.args))

    def test_namelist_is_not_len_two(self):

        """Function:  test_namelist_is_not_len_two

        Description:  Test name list is not a length of two.

        Arguments:

        """

        self.args.args_array["-M"] = ["Test_Repo_Name_1"]

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.rename_repo(self.els, args=self.args))

    def test_namelist_is_passed(self):

        """Function:  test_namelist_is_passed

        Description:  Test name list is passed as an argument.

        Arguments:

        """

        self.args.args_array = dict()

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.rename_repo(
                    self.els, name_list=["Test_Repo_Name_1"], args=self.args))

    def test_namelist_not_passed(self):

        """Function:  test_namelist_not_passed

        Description:  Test name list is not passed as an argument.

        Arguments:

        """

        self.args.args_array["-M"] = ["Test_Repo_Name_1"]

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.rename_repo(self.els, args=self.args))


if __name__ == "__main__":
    unittest.main()
