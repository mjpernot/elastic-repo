#!/usr/bin/python
# Classification (U)

"""Program:  delete_repo.py

    Description:  Unit testing of delete_repo in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/delete_repo.py

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
        test_err_flag_true -> Test err_flag is set to True.
        test_err_flag_false -> Test err_flag is set to False.
        test_repo_name_in_list -> Test repo name is in list.
        test_repo_name_not_in_list -> Test repo name is not in list.
        test_repo_name_is_passed -> Test repo name is passed as argument.
        test_repo_name_not_passed -> Test repo name is not passed as argument.

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
                delete_repo -> Mock of deleting a repository.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the class.

                Arguments:

                """

                self.repo_dict = ["Test_Repo_Name_1", "Test_Rep_Name_2",
                                  "Test_Repo_Name_False"]

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

                if repo_name == "Test_Repo_Name_False":
                    err_flag = True
                    err_msg = "Error_Message_Here"

                return err_flag, err_msg

        self.els = ElasticSearchRepo()

        self.args_array = {"-D": "Test_Repo_Name_1"}

    @unittest.skip("Known Bug: Requires the args_array to be passed.")
    def test_no_argsarray_is_passed(self):

        """Function:  test_no_argsarray_is_passed

        Description:  Test when args_array is not passed to function.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_repo(
                self.els, repo_name="Test_Repo_Name_3"))

    def test_err_flag_true(self):

        """Function:  test_err_flag_true

        Description:  Test err_flag is set to True.

        Arguments:

        """

        self.args_array["-D"] = "Test_Repo_Name_False"

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_repo(
                self.els, args_array=self.args_array))

    def test_err_flag_false(self):

        """Function:  test_err_flag_false

        Description:  Test err_flag is set to False.

        Arguments:

        """

        self.assertFalse(elastic_db_repo.delete_repo(
            self.els, args_array=self.args_array))

    def test_repo_name_in_list(self):

        """Function:  test_repo_name_in_list

        Description:  Test repo name is in list.

        Arguments:

        """

        self.assertFalse(elastic_db_repo.delete_repo(
            self.els, args_array=self.args_array))

    def test_repo_name_not_in_list(self):

        """Function:  test_repo_name_not_in_list

        Description:  Test repo name is not in list.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_repo(
                self.els, repo_name="Test_Repo_Name_3",
                args_array=self.args_array))

    def test_repo_name_is_passed(self):

        """Function:  test_repo_name_is_passed

        Description:  Test repo name is passed as an argument.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_repo(
                self.els, repo_name="Test_Repo_Name_3", args_array={}))

    def test_repo_name_not_passed(self):

        """Function:  test_repo_name_not_passed

        Description:  Test repo name is not passed as an argument.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_repo(
                self.els, args_array={"-D": "Test_Repo_Name_3"}))


if __name__ == "__main__":
    unittest.main()
