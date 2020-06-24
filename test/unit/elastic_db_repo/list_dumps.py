#!/usr/bin/python
# Classification (U)

"""Program:  list_dumps.py

    Description:  Unit testing of list_dumps in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/list_dumps.py

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
        setUp -> Unit testing initilization.
        test_repo_name -> Test with repo name present.
        test_repo_empty_list -> Test repo dict is an empty list.
        test_repo_name_false -> Test repo name set to None.
        test_repo_name_miss -> Test with repo name not present.

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

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the class.

                Arguments:

                """

                self.els = "Elastic_Search_Class"
                self.repo = "Test_Repo_Name"
                self.dump_list = []
                self.repo_dict = ["TEST_REPO", "TEST_REPO2"]

        self.els = ElasticSearchRepo()

    @mock.patch("elastic_db_repo.elastic_class")
    @mock.patch("elastic_db_repo.elastic_libs")
    def test_repo_name(self, mock_libs, mock_cls):

        """Function:  test_repo_name

        Description:  Test with repo name present.

        Arguments:

        """

        self.els.repo = "TEST_REPO2"

        mock_libs.get_dump_list.return_value = True
        mock_cls.list_dumps.return_value = []

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.list_dumps(self.els))

    @mock.patch("elastic_db_repo.elastic_class")
    @mock.patch("elastic_db_repo.elastic_libs")
    def test_repo_empty_list(self, mock_libs, mock_cls):

        """Function:  test_repo_empty_list

        Description:  Test repo dict is an empty list.

        Arguments:

        """

        self.els.repo = None
        self.els.repo_dict = []

        mock_libs.get_dump_list.return_value = True
        mock_cls.list_dumps.return_value = []

        self.assertFalse(elastic_db_repo.list_dumps(self.els))

    @mock.patch("elastic_db_repo.elastic_class")
    @mock.patch("elastic_db_repo.elastic_libs")
    def test_repo_name_false(self, mock_libs, mock_cls):

        """Function:  test_repo_name_false

        Description:  Test repo name set to None.

        Arguments:

        """

        self.els.repo = None

        mock_libs.get_dump_list.return_value = True
        mock_cls.list_dumps.return_value = []

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.list_dumps(self.els))

    @mock.patch("elastic_db_repo.elastic_class")
    @mock.patch("elastic_db_repo.elastic_libs")
    def test_repo_name_miss(self, mock_libs, mock_cls):

        """Function:  test_repo_name_miss

        Description:  Test with repo name not present.

        Arguments:

        """

        mock_libs.get_dump_list.return_value = True
        mock_cls.list_dumps.return_value = []

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.list_dumps(self.els))


if __name__ == "__main__":
    unittest.main()
