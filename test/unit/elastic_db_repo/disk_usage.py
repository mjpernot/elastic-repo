#!/usr/bin/python
# Classification (U)

"""Program:  disk_usage.py

    Description:  Unit testing of disk_usage in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/disk_usage.py

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
import collections
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
        test_repodict_multiple_entries -> Test repo_dict has multiple entries.
        test_repodict_one_entry -> Test repo_dict has one entry.
        test_repodict_empty -> Test repo_dict is empty.

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

                self.repo_dict = {
                    "Test_Repo_Name_1": {
                        "type": "fs", "settings": {
                            "compress": "true",
                            "location": "/dir/TEST_REPO1"}}}
                self.repo_dict2 = {
                    "Test_Repo_Name_1": {
                        "type": "fs", "settings": {
                            "compress": "true",
                            "location": "/dir/TEST_REPO1"}},
                    "Test_Repo_Name_2": {
                        "type": "fs", "settings": {
                            "compress": "true",
                            "location": "/dir/TEST_REPO2"}}}

        self.els = ElasticSearchRepo()

    @mock.patch("elastic_db_repo.gen_libs")
    def test_repodict_multiple_entries(self, mock_lib):

        """Function:  test_repodict_multiple_entries

        Description:  Test repo_dict has multiple entries.

        Arguments:

        """

        self.els.repo_dict = self.els.repo_dict2
        _ntuple_diskusage = collections.namedtuple("usage", "total used free")

        mock_lib.disk_usage.side_effect = [_ntuple_diskusage(total=1023303680,
                                                             used=703119360,
                                                             free=266498048),
                                           _ntuple_diskusage(total=1023303681,
                                                             used=703119361,
                                                             free=266498049)]
        mock_lib.bytes_2_readable.side_effect = ["975.90MB",
                                                 "670.55MB",
                                                 "254.15MB",
                                                 "975.91MB",
                                                 "670.56MB",
                                                 "254.16MB"]

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.disk_usage(self.els))

    @mock.patch("elastic_db_repo.gen_libs")
    def test_repodict_one_entry(self, mock_lib):

        """Function:  test_repodict_one_entry

        Description:  Test repo_dict has one entry.

        Arguments:

        """

        _ntuple_diskusage = collections.namedtuple("usage", "total used free")

        mock_lib.disk_usage.return_value = _ntuple_diskusage(total=1023303680,
                                                             used=703119360,
                                                             free=266498048)
        mock_lib.bytes_2_readable.side_effect = ["975.90MB", "670.55MB",
                                                 "254.15MB"]

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.disk_usage(self.els))

    def test_repodict_empty(self):

        """Function:  test_repodict_empty

        Description:  Test repo_dict is empty.

        Arguments:

        """

        self.els.repo_dict = {}

        self.assertFalse(elastic_db_repo.disk_usage(self.els))


if __name__ == "__main__":
    unittest.main()
