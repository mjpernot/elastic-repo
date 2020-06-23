#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_repo
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialization for unit testing.
        test_list_repos -> Test list_repos function.

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

                self.repo_dict = {"Test_Repo_Name_1": {
                    "type": "fs", "settings": {"compress": "true",
                                               "location": "/dir/TEST_REPO1"}}}

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
