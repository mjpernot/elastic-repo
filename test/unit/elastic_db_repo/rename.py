# Classification (U)

"""Program:  rename.py

    Description:  Unit testing of _rename in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/rename.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_delete_err_false
        test_delete_err_true
        test_create_err_false
        test_create_err_true

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

        self.els = ElasticSearchRepo()

        self.name_list = ["Test_Repo_Name_1", "Test_Dump_Name_5"]
        self.name_list2 = ["Test_Repo_Name_2", "Test_Repo_Name_5"]
        self.name_list3 = ["Test_Repo_Name_1", "Test_Repo_Name_5"]
        self.name_list4 = ["Test_Repo_Name_1", "Test_Repo_Name_F"]

    def test_delete_err_false(self):

        """Function:  test_delete_err_false

        Description:  Test delete repo returns error flag is false.

        Arguments:

        """

        self.assertFalse(elastic_db_repo._rename(self.els, self.name_list))

    def test_delete_err_true(self):

        """Function:  test_delete_err_true

        Description:  Test delete repo returns error flag is true.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo._rename(self.els,
                                                     self.name_list2))

    def test_create_err_false(self):

        """Function:  test_create_err_false

        Description:  Test create repo returns error flag is false.

        Arguments:

        """

        self.assertFalse(elastic_db_repo._rename(self.els, self.name_list3))

    def test_create_err_true(self):

        """Function:  test_create_err_true

        Description:  Test create repo returns error flag is true.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo._rename(self.els,
                                                     self.name_list4))


if __name__ == "__main__":
    unittest.main()
