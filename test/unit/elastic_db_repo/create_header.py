# Classification (U)

"""Program:  create_header.py

    Description:  Unit testing of create_header in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/create_header.py

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
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_check_header
        test_base_header

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.name = "Repo"
        self.results = "Elastic_Repo"
        self.results2 = "Repo"

    def test_check_header(self):

        """Function:  test_check_header

        Description:  Test with check added to header.

        Arguments:

        """

        self.assertEqual(
            elastic_db_repo.create_header(self.dtg, name=self.name)["Check"],
            self.results2)

    def test_base_header(self):

        """Function:  test_base_header

        Description:  Test with base header.

        Arguments:

        """

        self.assertEqual(
            elastic_db_repo.create_header(self.dtg)["Application"],
            self.results)


if __name__ == "__main__":
    unittest.main()
