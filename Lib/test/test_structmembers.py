from _testcapi import test_structmembersType, \
    CHAR_MAX, CHAR_MIN, UCHAR_MAX, \
    SHRT_MAX, SHRT_MIN, USHRT_MAX, \
    INT_MAX, INT_MIN, UINT_MAX, \
    LONG_MAX, LONG_MIN, ULONG_MAX, \
    LLONG_MAX, LLONG_MIN, ULLONG_MAX, \
    PY_SSIZE_T_MAX, PY_SSIZE_T_MIN

import unittest
from test import support

ts=test_structmembersType(False,  # T_BOOL
                          1,      # T_BYTE
                          2,      # T_UBYTE
                          3,      # T_SHORT
                          4,      # T_USHORT
                          5,      # T_INT
                          6,      # T_UINT
                          7,      # T_LONG
                          8,      # T_ULONG
                          23,     # T_PYSSIZET
                          9.99999,# T_FLOAT
                          10.1010101010 # T_DOUBLE
                          )

class ReadWriteTests(unittest.TestCase):
    def test_types(self):
        ts.T_BOOL = True
        self.assertEquals(ts.T_BOOL, True)
        ts.T_BOOL = False
        self.assertEquals(ts.T_BOOL, False)
        self.assertRaises(TypeError, setattr, ts, 'T_BOOL', 1)

        ts.T_BYTE = CHAR_MAX
        self.assertEquals(ts.T_BYTE, CHAR_MAX)
        ts.T_BYTE = CHAR_MIN
        self.assertEquals(ts.T_BYTE, CHAR_MIN)
        ts.T_UBYTE = UCHAR_MAX
        self.assertEquals(ts.T_UBYTE, UCHAR_MAX)

        ts.T_SHORT = SHRT_MAX
        self.assertEquals(ts.T_SHORT, SHRT_MAX)
        ts.T_SHORT = SHRT_MIN
        self.assertEquals(ts.T_SHORT, SHRT_MIN)
        ts.T_USHORT = USHRT_MAX
        self.assertEquals(ts.T_USHORT, USHRT_MAX)

        ts.T_INT = INT_MAX
        self.assertEquals(ts.T_INT, INT_MAX)
        ts.T_INT = INT_MIN
        self.assertEquals(ts.T_INT, INT_MIN)
        ts.T_UINT = UINT_MAX
        self.assertEquals(ts.T_UINT, UINT_MAX)

        ts.T_LONG = LONG_MAX
        self.assertEquals(ts.T_LONG, LONG_MAX)
        ts.T_LONG = LONG_MIN
        self.assertEquals(ts.T_LONG, LONG_MIN)
        ts.T_ULONG = ULONG_MAX
        self.assertEquals(ts.T_ULONG, ULONG_MAX)

        ts.T_PYSSIZET = PY_SSIZE_T_MAX
        self.assertEquals(ts.T_PYSSIZET, PY_SSIZE_T_MAX)
        ts.T_PYSSIZET = PY_SSIZE_T_MIN
        self.assertEquals(ts.T_PYSSIZET, PY_SSIZE_T_MIN)

        ## T_LONGLONG and T_ULONGLONG may not be present on some platforms
        if hasattr(ts, 'T_LONGLONG'):
            ts.T_LONGLONG = LLONG_MAX
            self.assertEquals(ts.T_LONGLONG, LLONG_MAX)
            ts.T_LONGLONG = LLONG_MIN
            self.assertEquals(ts.T_LONGLONG, LLONG_MIN)

            ts.T_ULONGLONG = ULLONG_MAX
            self.assertEquals(ts.T_ULONGLONG, ULLONG_MAX)

            ## make sure these will accept a plain int as well as a long
            ts.T_LONGLONG = 3
            self.assertEquals(ts.T_LONGLONG, 3)
            ts.T_ULONGLONG = 4
            self.assertEquals(ts.T_ULONGLONG, 4)

    def test_bad_assignments(self):
        # XXX testing of T_UINT and T_ULONG temporarily disabled;
        # see issue 8014.
        integer_attributes = [
            'T_BOOL',
            'T_BYTE', 'T_UBYTE',
            'T_SHORT', 'T_USHORT',
            'T_INT', 'T_UINT',
            'T_LONG', 'T_ULONG',
            'T_PYSSIZET'
            ]

        if hasattr(ts, 'T_LONGLONG'):
            integer_attributes.extend(['T_LONGLONG', 'T_ULONGLONG'])

        # issue8014: this produced 'bad argument to internal function'
        # internal error
        for nonint in None, 3.2j, "full of eels", {}, []:
            for attr in integer_attributes:
                self.assertRaises(TypeError, setattr, ts, attr, nonint)


class TestWarnings(unittest.TestCase):

    def test_byte_max(self):
        with support.check_warnings(('', RuntimeWarning)):
            ts.T_BYTE = CHAR_MAX+1

    def test_byte_min(self):
        with support.check_warnings(('', RuntimeWarning)):
            ts.T_BYTE = CHAR_MIN-1

    def test_ubyte_max(self):
        with support.check_warnings(('', RuntimeWarning)):
            ts.T_UBYTE = UCHAR_MAX+1

    def test_short_max(self):
        with support.check_warnings(('', RuntimeWarning)):
            ts.T_SHORT = SHRT_MAX+1

    def test_short_min(self):
        with support.check_warnings(('', RuntimeWarning)):
            ts.T_SHORT = SHRT_MIN-1

    def test_ushort_max(self):
        with support.check_warnings(('', RuntimeWarning)):
            ts.T_USHORT = USHRT_MAX+1


def test_main(verbose=None):
    support.run_unittest(__name__)

if __name__ == "__main__":
    test_main(verbose=True)
