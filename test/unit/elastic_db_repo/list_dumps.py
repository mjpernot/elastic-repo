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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import elastic_db_repo                          # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

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

        self.args_array = {}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class ElasticSearchRepo():                              # pylint:disable=R0903

    """Class:  ElasticSearchRepo

    Description:  Class representation of the ElasticSearchRepo class.

    Methods:
        __init__
        get_repo_list

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the class.

        Arguments:

        """

        self.hosts = ["https://nodename1:9200", "https://nodename2:9200"]
        self.repo_dict = {"reponame": "Repo", "reponame2": "Repo"}

    def get_repo_list(self):

        """Method:  get_repo_list

        Description:  Return repositiory list.

        Arguments:

        """

        return self.repo_dict


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_repo_incorrect
        test_no_repo
        test_repo

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.els = ElasticSearchRepo()
        self.args = ArgParser()

    @mock.patch("elastic_db_repo.data_out", mock.Mock(return_value=True))
    @mock.patch("elastic_db_repo.create_header",
                mock.Mock(return_value={"Header": "DTG"}))
    def test_repo_incorrect(self):

        """Function:  test_repo_incorrect

        Description:  Test with incorrect repo name.

        Arguments:

        """

        self.args.args_array = {"-L": "reponame3"}

        with gen_libs.no_std_out():
            self.assertFalse(
                elastic_db_repo.list_dumps(self.els, args=self.args))

    @mock.patch("elastic_db_repo.data_out", mock.Mock(return_value=True))
    @mock.patch("elastic_db_repo.get_dumps",
                mock.Mock(return_value={"key": "data"}))
    @mock.patch("elastic_db_repo.create_header",
                mock.Mock(return_value={"Header": "DTG"}))
    def test_no_repo(self):

        """Function:  test_no_repo

        Description:  Test with no repo name passed.

        Arguments:

        """

        self.args.args_array = {"-L": None}

        self.assertFalse(
            elastic_db_repo.list_dumps(self.els, args=self.args))

    @mock.patch("elastic_db_repo.data_out", mock.Mock(return_value=True))
    @mock.patch("elastic_db_repo.get_dumps",
                mock.Mock(return_value={"key": "data"}))
    @mock.patch("elastic_db_repo.create_header",
                mock.Mock(return_value={"Header": "DTG"}))
    def test_repo(self):

        """Function:  test_repo

        Description:  Test with repo name passed.

        Arguments:

        """

        self.args.args_array = {"-L": "reponame"}

        self.assertFalse(
            elastic_db_repo.list_dumps(self.els, args=self.args))


if __name__ == "__main__":
    unittest.main()
