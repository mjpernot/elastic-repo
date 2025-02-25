# Classification (U)

"""Program:  list_repos.py

    Description:  Unit testing of list_repos in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/list_repos.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_repo                          # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ElasticSearchRepo():                              # pylint:disable=R0903

    """Class:  ElasticSearchRepo

    Description:  Class representation of the ElasticSearchRepo class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.repo_dict = {"Test_Repo_Name_1": {
            "type": "fs", "settings": {"compress": "true",
                                       "location": "/dir/TEST_REPO1"}}}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_list_repos

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearchRepo()

    @mock.patch("elastic_db_repo.elastic_libs.list_repos2")
    def test_list_repos(self, mock_list):

        """Function:  test_list_repos

        Description:  Test list_repos function.

        Arguments:

        """

        mock_list.return_value = True

        self.assertFalse(elastic_db_repo.list_repos(self.els))


if __name__ == "__main__":
    unittest.main()
