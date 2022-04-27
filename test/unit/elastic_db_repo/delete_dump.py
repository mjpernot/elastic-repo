#!/usr/bin/python
# Classification (U)

"""Program:  delete_dump.py

    Description:  Unit testing of delete_dump in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/delete_dump.py

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
import mock

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
        setUp
        test_status_false
        test_status_true
        test_err_flag_true
        test_err_flag_false
        test_dump_name_in_list
        test_dump_name_not_in_list
        test_repo_name_in_list
        test_repo_name_not_in_list
        test_dump_name_is_passed
        test_dump_name_not_passed
        test_repo_name_is_passed
        test_repo_name_not_passed

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
                __init__
                delete_repo

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the class.

                Arguments:

                """

                self.els = "Elastic_Search_Class"
                self.repo_dict = ["Test_Repo_Name_1", "Test_Rep_Name_2"]
                self.repo_name = None

            def delete_dump(self, repo_name, dump_name):

                """Method:  delete_repo

                Description:  Mock of deleting a repository.

                Arguments:

                """

                self.repo_name = repo_name
                err_flag = False
                err_msg = None

                if dump_name == "Test_Dump_Name_Fail":
                    err_flag = True
                    err_msg = "Error_Message_Here"

                return err_flag, err_msg

        self.els = ElasticSearchRepo()
        self.args_array = {"-r": "Test_Repo_Name_1", "-S": "Test_Dump_Name_1"}
        self.results = (
            [{"snapshot": "Test_Dump_Name_1"},
             {"snapshot": "Test_Dump_Name_2"}], True, None)
        self.results2 = (
            [{"snapshot": "Test_Dump_Name_1"},
             {"snapshot": "Test_Dump_Name_2"},
             {"snapshot": "Test_Dump_Name_Fail"}], True, None)
        self.results3 = (
            [{"snapshot": "Test_Dump_Name_1"},
             {"snapshot": "Test_Dump_Name_2"}], False, "Error Message Here")

    @mock.patch("elastic_db_repo.elastic_class")
    def test_status_false(self, mock_class):

        """Function:  test_status_false

        Description:  Test status returns false.

        Arguments:

        """

        mock_class.get_dump_list.return_value = self.results3

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_dump(
                self.els, args_array=self.args_array))

    @mock.patch("elastic_db_repo.elastic_class")
    def test_status_true(self, mock_class):

        """Function:  test_status_true

        Description:  Test status returns true.

        Arguments:

        """

        mock_class.get_dump_list.return_value = self.results

        self.assertFalse(elastic_db_repo.delete_dump(
            self.els, args_array=self.args_array))

    @mock.patch("elastic_db_repo.elastic_class")
    def test_err_flag_true(self, mock_class):

        """Function:  test_err_flag_true

        Description:  Test err_flag is set to True.

        Arguments:

        """

        mock_class.get_dump_list.return_value = self.results2

        self.args_array["-S"] = "Test_Dump_Name_Fail"

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_dump(
                self.els, args_array=self.args_array))

    @mock.patch("elastic_db_repo.elastic_class")
    def test_err_flag_false(self, mock_class):

        """Function:  test_err_flag_false

        Description:  Test err_flag is set to False.

        Arguments:

        """

        mock_class.get_dump_list.return_value = self.results

        self.assertFalse(elastic_db_repo.delete_dump(
            self.els, args_array=self.args_array))

    @mock.patch("elastic_db_repo.elastic_class")
    def test_dump_name_in_list(self, mock_class):

        """Function:  test_dump_name_in_list

        Description:  Test dump name is in list.

        Arguments:

        """

        mock_class.get_dump_list.return_value = self.results

        self.assertFalse(elastic_db_repo.delete_dump(
            self.els, args_array=self.args_array))

    @mock.patch("elastic_db_repo.elastic_class")
    def test_dump_name_not_in_list(self, mock_class):

        """Function:  test_dump_name_not_in_list

        Description:  Test dump name is not in list.

        Arguments:

        """

        mock_class.get_dump_list.return_value = self.results

        self.args_array["-S"] = "Test_Dump_Name_3"

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_dump(
                self.els, args_array=self.args_array))

    @mock.patch("elastic_db_repo.elastic_class")
    def test_repo_name_in_list(self, mock_class):

        """Function:  test_repo_name_in_list

        Description:  Test repo name is in list.

        Arguments:

        """

        mock_class.get_dump_list.return_value = self.results

        self.args_array["-S"] = "Test_Dump_Name_3"

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_dump(
                self.els, args_array=self.args_array))

    def test_repo_name_not_in_list(self):

        """Function:  test_repo_name_not_in_list

        Description:  Test repo name is not in list.

        Arguments:

        """

        self.args_array["-r"] = "Test_Repo_Name_3"

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_dump(
                self.els, args_array=self.args_array))

    @mock.patch("elastic_db_repo.elastic_class")
    def test_dump_name_is_passed(self, mock_class):

        """Function:  test_repo_name_not_passed

        Description:  Test dump name is passed as an argument.

        Arguments:

        """

        mock_class.get_dump_list.return_value = self.results

        self.args_array["-r"] = "Test_Repo_Name_1"

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_dump(
                self.els, dump_name="Test_Dump_Name_3",
                args_array=self.args_array))

    @mock.patch("elastic_db_repo.elastic_class")
    def test_dump_name_not_passed(self, mock_class):

        """Function:  test_dump_name_not_passed

        Description:  Test dump name is not passed as an argument.

        Arguments:

        """

        mock_class.get_dump_list.return_value = self.results

        self.args_array["-S"] = "Test_Dump_Name_3"

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_dump(
                self.els, args_array=self.args_array))

    def test_repo_name_is_passed(self):

        """Function:  test_repo_name_is_passed

        Description:  Test repo name is passed as an argument.

        Arguments:

        """

        self.args_array = {"-S": "Test_Dump_Name_1"}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_dump(
                self.els, repo_name="Test_Repo_Name_3",
                args_array=self.args_array))

    def test_repo_name_not_passed(self):

        """Function:  test_repo_name_not_passed

        Description:  Test repo name is not passed as an argument.

        Arguments:

        """

        self.args_array["-r"] = "Test_Repo_Name_3"

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.delete_dump(
                self.els, args_array=self.args_array))


if __name__ == "__main__":
    unittest.main()
