# Classification (U)

"""Program:  get_dumps.py

    Description:  Unit testing of get_dumps in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/get_dumps.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import elastic_db_repo                         # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ElasticSearch():                                  # pylint:disable=R0903

    """Class:  ElasticSearch

    Description:  Class representation of the ElasticSearch class.

    Methods:
        __init__
        get_repo_list

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.els = "Elasticsearch class instance"
        self.hosts = ["https://nodename1:9200", "https://nodename2:9200"]
        self.repo = None
        self.dump_list = None

    def get_dump_list(self, repo):

        """Method:  get_dump_list

        Description:  Return dump list.

        Arguments:

        """

        self.repo = repo

        return self.dump_list


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_dumps

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        dump_list = [[
            {"state": "SUCCESS", "start_time": "2025-08-19T11:05:11.308Z",
             "shards": {"successful": 4, "failed": 0, "total": 4},
             "snapshot": "spock_bkp_20250819-110511"},
            {"state": "FAILED", "start_time": "2025-08-19T12:05:12.012Z",
             "shards": {"successful": 0, "failed": 4, "total": 4},
             "snapshot": "spock_bkp_20250819-120512"},
            {"state": "SUCCESS", "start_time": "2025-08-19T14:05:14.140Z",
             "shards": {"successful": 4, "failed": 0, "total": 4},
             "snapshot": "spock_bkp_20250820-140514"}]]
        self.els = ElasticSearch()
        self.els.dump_list = dump_list
        self.repo = "RepoName"

    def test_dumps(self):

        """Function:  test_dumps

        Description:  Test with returning all dumps.

        Arguments:

        """

        self.assertEqual(
            len(elastic_db_repo.get_dumps(
                self.els, repo=self.repo)[self.repo]), 3)


if __name__ == "__main__":
    unittest.main()
