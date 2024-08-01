# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/main.py

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
import elastic_db_repo
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_cond_req_or
        arg_dir_chk
        arg_require
        arg_xor_dict
        arg_parse2

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()
        self.opt_req = None
        self.opt_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True
        self.opt_con_or = None
        self.opt_con_or2 = True
        self.opt_xor_val = None
        self.opt_xor_val2 = True
        self.argparse2 = True

    def arg_cond_req_or(self, opt_con_or):

        """Method:  arg_cond_req_or

        Description:  Method stub holder for
            gen_class.ArgParser.arg_cond_req_or.

        Arguments:

        """

        self.opt_con_or = opt_con_or

        return self.opt_con_or2

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def arg_xor_dict(self, opt_xor_val):

        """Method:  arg_xor_dict

        Description:  Method stub holder for gen_class.ArgParser.arg_xor_dict.

        Arguments:

        """

        self.opt_xor_val = opt_xor_val

        return self.opt_xor_val2

    def arg_parse2(self):

        """Method:  arg_parse2

        Description:  Method stub holder for gen_class.ArgParser.arg_parse2.

        Arguments:

        """

        return self.argparse2


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_arg_parse2_false
        test_arg_parse2_true
        test_help_true
        test_help_false
        test_require_false
        test_require_true
        test_xor_dict_false
        test_xor_dict_true
        test_con_req_or_false
        test_con_req_or_true
        test_arg_dir_chk_false
        test_arg_dir_chk_true
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args.args_array = {
            "-c": "config_file", "-d": "config_dir", "-R": True}

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_arg_parse2_false(self, mock_arg, mock_help):

        """Function:  test_arg_parse2_false

        Description:  Test arg_parser2 returns false.

        Arguments:

        """

        self.args.argparse2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_arg_parse2_true(self, mock_arg, mock_help):

        """Function:  test_arg_parse2_true

        Description:  Test arg_parser2 returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test with help_func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test with help_func returns False.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_require_false(self, mock_arg, mock_help):

        """Function:  test_require_false

        Description:  Test with arg_require returns False.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_require_true(self, mock_arg, mock_help):

        """Function:  test_require_true

        Description:  Test with arg_require returns True.

        Arguments:

        """

        self.args.opt_xor_val2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_xor_dict_false(self, mock_arg, mock_help):

        """Function:  test_xor_dict_false

        Description:  Test with arg_xor_dict returns False.

        Arguments:

        """

        self.args.opt_xor_val2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_xor_dict_true(self, mock_arg, mock_help):

        """Function:  test_xor_dict_true

        Description:  Test with arg_xor_dict returns True.

        Arguments:

        """

        self.args.opt_con_or2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_con_req_or_false(self, mock_arg, mock_help):

        """Function:  test_con_req_or_false

        Description:  Test with arg_cond_req_or returns False.

        Arguments:

        """

        self.args.opt_con_or2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_con_req_or_true(self, mock_arg, mock_help):

        """Function:  test_con_req_or_true

        Description:  Test with arg_cond_req_or returns True.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_arg_dir_chk_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_false

        Description:  Test with arg_dir_chk returns False.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.run_program", mock.Mock(return_value=True))
    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_arg_dir_chk_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_true

        Description:  Test with arg_dir_chk returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())

    @mock.patch("elastic_db_repo.run_program", mock.Mock(return_value=True))
    @mock.patch("elastic_db_repo.gen_libs.help_func")
    @mock.patch("elastic_db_repo.gen_class.ArgParser")
    def test_run_program(self, mock_arg, mock_help):

        """Function:  test_run_program

        Description:  Test with calling run_program.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = False

        self.assertFalse(elastic_db_repo.main())


if __name__ == "__main__":
    unittest.main()
