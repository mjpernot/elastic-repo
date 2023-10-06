# Classification (U)

"""Program:  create_repo.py

    Description:  Unit testing of create_repo in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/create_repo.py

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

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.repo_dict = ["Test_Repo_Name_1", "Test_Rep_Name_2"]
        self.repo_dir = None

    def create_repo(self, repo_name, repo_dir):

        """Method:  create_repo

        Description:  Mock of creating a repository.

        Arguments:

        """

        self.repo_dir = repo_dir
        err_flag = False
        err_msg = None

        if repo_name == "Test_Repo_Name_False":
            err_flag = True
            err_msg = "Error_Message_Here"

        return err_flag, err_msg


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_err_flag_true
        test_err_flag_false
        test_repo_name_not_in_list
        test_repo_name_in_list
        test_repo_name_is_passed
        test_repo_name_not_passed

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearchRepo()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {
            "-C": "Test_Repo_Name_3", "-l": "Repo_Directory"}
        self.args2.args_array = {"-l": "Repo_Directory"}

    def test_err_flag_true(self):

        """Function:  test_err_flag_true

        Description:  Test err_flag is set to True.

        Arguments:

        """

        self.args.args_array["-C"] = "Test_Repo_Name_False"

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.create_repo(self.els, args=self.args))

    def test_err_flag_false(self):

        """Function:  test_err_flag_false

        Description:  Test err_flag is set to False.

        Arguments:

        """

        self.assertFalse(elastic_db_repo.create_repo(self.els, args=self.args))

    def test_repo_name_not_in_list(self):

        """Function:  test_repo_name_not_in_list

        Description:  Test repo name is not in list.

        Arguments:

        """

        self.assertFalse(elastic_db_repo.create_repo(self.els, args=self.args))

    def test_repo_name_in_list(self):

        """Function:  test_repo_name_in_list

        Description:  Test repo name is in list.

        Arguments:

        """

        self.args.args_array["-C"] = "Test_Repo_Name_1"

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.create_repo(self.els, args=self.args))

    def test_repo_name_is_passed(self):

        """Function:  test_repo_name_is_passed

        Description:  Test repo name is passed as an argument.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.create_repo(
                    self.els, repo_name="Test_Repo_Name_1", args=self.args2))

    def test_repo_name_not_passed(self):

        """Function:  test_repo_name_not_passed

        Description:  Test repo name is not passed as an argument.

        Arguments:

        """

        self.args.args_array["-C"] = "Test_Repo_Name_1"

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.create_repo(self.els, args=self.args))


if __name__ == "__main__":
    unittest.main()
