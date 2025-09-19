# Classification (U)

"""Program:  data_out.py

    Description:  Unit testing of data_out in elastic_db_repo.py.

    Usage:
        test/unit/elastic_db_repo/data_out.py

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
import elastic_db_repo                         # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "elastic", "-d": "config"}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class Mail():

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.data = None

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        self.data = data

        return True

    def send_mail(self, use_mailx=False):

        """Method:  send_mail

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        status = True

        if use_mailx:
            status = True

        return status


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_outfile_append_mode_expand
        test_outfile_write_mode_expand
        test_outfile_expand
        test_outfile_append_mode
        test_outfile_write_mode
        test_outfile
        test_email_subj
        test_email_no_subj
        test_email_mailx
        test_email_indent
        test_email
        test_indent_true
        test_indent_false
        test_suppress_true
        test_suppress_false_no_expand
        test_suppress_false_expand
        test_not_dictionary
        test_no_data

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.data = {"key1": "value1", "key2": "value2"}
        self.mail = Mail()
        self.args = ArgParser()
        self.outfile = "path/to/open"

    @mock.patch("elastic_db_repo.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_append_mode_expand(self, mock_file):

        """Function:  test_outfile_append_mode_expand

        Description:  Test with outfile and expand and append option.

        Arguments:

        """

        self.args.args_array = {
            "-o": self.outfile, "-a": True, "-j": True, "-z": True}

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_write_mode_expand(self, mock_file):

        """Function:  test_outfile_write_mode_expand

        Description:  Test with outfile and expand and write option.

        Arguments:

        """

        self.args.args_array = {"-o": self.outfile, "-j": True, "-z": True}

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_expand(self, mock_file):

        """Function:  test_outfile_expand

        Description:  Test with outfile and expand option.

        Arguments:

        """

        self.args.args_array = {"-o": self.outfile, "-j": True, "-z": True}

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_append_mode(self, mock_file):

        """Function:  test_outfile_append_mode

        Description:  Test with outfile and append mode option.

        Arguments:

        """

        self.args.args_array = {"-o": self.outfile, "-a": True, "-z": True}

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile_write_mode(self, mock_file):

        """Function:  test_outfile_write_mode

        Description:  Test with outfile and write mode option.

        Arguments:

        """

        self.args.args_array = {"-o": self.outfile, "-z": True}

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.pprint.pprint", mock.Mock(return_value=True))
    @mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
    def test_outfile(self, mock_file):

        """Function:  test_outfile

        Description:  Test with outfile option.

        Arguments:

        """

        self.args.args_array = {"-o": self.outfile, "-z": True}

        assert open(                            # pylint:disable=R1732,W1514
            self.outfile).read() == "data"
        mock_file.assert_called_with(self.outfile)

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.gen_class.setup_mail")
    def test_email_subj(self, mock_mail):

        """Function:  test_email_subj

        Description:  Test with email option with subject option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.args.args_array = {
            "-t": "to_address", "-s": "subject", "-z": True}

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.gen_class.setup_mail")
    def test_email_no_subj(self, mock_mail):

        """Function:  test_email_no_subj

        Description:  Test with email option with no subject option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.args.args_array = {"-t": "to_address", "-z": True}

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.gen_class.setup_mail")
    def test_email_mailx(self, mock_mail):

        """Function:  test_email_mailx

        Description:  Test with email option with mailx option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.args.args_array = {
            "-t": "to_address", "-j": True, "-x": True, "-z": True}

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.gen_class.setup_mail")
    def test_email_indent(self, mock_mail):

        """Function:  test_email_indent

        Description:  Test with email option with indent.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.args.args_array = {"-t": "to_address", "-j": True, "-z": True}

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    @mock.patch("elastic_db_repo.gen_class.setup_mail")
    def test_email(self, mock_mail):

        """Function:  test_email

        Description:  Test with email option.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.args.args_array = {"-t": "to_address", "-z": True}

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    def test_indent_true(self):

        """Function:  test_indent_true

        Description:  Test with indent arg passed in.

        Arguments:

        """

        self.args.args_array = {"-j": True}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    def test_indent_false(self):

        """Function:  test_indent_false

        Description:  Test with no indent arg passed in.

        Arguments:

        """

        self.args.args_array = {}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    def test_suppress_true(self):

        """Function:  test_suppress_true

        Description:  Test with suppression is true.

        Arguments:

        """

        self.args.args_array = {"-z": True}

        self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    def test_suppress_false_no_expand(self):

        """Function:  test_suppress_false_no_expand

        Description:  Test with suppression is false and no expand option.

        Arguments:

        """

        self.args.args_array = {}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    def test_suppress_false_expand(self):

        """Function:  test_suppress_false_expand

        Description:  Test with suppression is false and expand option.

        Arguments:

        """

        self.args.args_array = {"-j": True}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.data_out(self.data, self.args))

    def test_not_dictionary(self):

        """Function:  test_not_dictionary

        Description:  Test data is not a dictionary.

        Arguments:

        """

        self.args.args_array = {"-z": True}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.data_out("datastr", self.args))

    def test_no_data(self):

        """Function:  test_no_data

        Description:  Test with no data send to function.

        Arguments:

        """

        self.args.args_array = {"-z": True}

        with gen_libs.no_std_out():
            self.assertFalse(elastic_db_repo.data_out("", self.args))


if __name__ == "__main__":
    unittest.main()
