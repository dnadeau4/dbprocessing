#!/usr/bin/env python2.6

"""Unit tests for string handling for dbprocessing"""

__author__ = 'Jonathan Niehof <jniehof@lanl.gov>'
__version__ = '0.0'

import unittest

import DBStrings


class DBFormatterTests(unittest.TestCase):
    """Tests of the revised Formatter class

    @ivar fmtr: instance of the revised formatter
    @type fmtr: DBStrings.DBFormatter
    """

    def __init__(self, *args, **kwargs):
        """Create a formatter object"""
        super(DBFormatterTests, self).__init__(*args, **kwargs)
        self.fmtr = DBStrings.DBFormatter()

    def testNormalFormatting(self):
        """Format some strings that are same as normal formatter"""
        self.assertEqual('hi there',
                         self.fmtr.format('hi {a}', a='there'))
        self.assertEqual('hi there',
                         self.fmtr.format('hi {0}', 'there'))
        self.assertEqual('0003.20 hi',
                         self.fmtr.format('{1:07.2f} {0}', 'hi', 3.2))

    def testMissingKey(self):
        """Format strings with unspecified keys"""
        self.assertEqual('hi {there}',
                         self.fmtr.format('{hi} {there}', hi='hi'))
        self.assertEqual(
            'hi {there.here!s:100s}',
            self.fmtr.format('{hi} {there.here!s:100s}', hi='hi'))

    def testAssemble(self):
        """Assemble components of a field spec"""
        self.assertEqual('{04d}',
                         self.fmtr.assemble('', '', '04d', ''))
        self.assertEqual('stuff{name[0]!s:4.2f}',
                         self.fmtr.assemble('stuff', 'name[0]', '4.2f', 's'))


class UnfoundFieldTests(unittest.TestCase):
    """Tests of the UnfoundField object"""

    def testSetKey(self):
        """Record key name on not-found object"""
        a = DBStrings._UnfoundField('key')
        self.assertEqual('key', a.key)

    def testGetattr(self):
        """Record an attribute lookup on the not-found object"""
        a = DBStrings._UnfoundField('key')
        b = a.attr
        self.assertEqual(a, b)
        self.assertEqual(a.lookups, '.attr')

    def testGetItem(self):
        """Record an item lookup on the not-found object"""
        a = DBStrings._UnfoundField('key')
        b = a['keyname']
        self.assertEqual(a, b)
        self.assertEqual(a.lookups, "['keyname']")
        c = b[0]
        self.assertEqual(a, c)
        self.assertEqual(a.lookups, "['keyname'][0]")

    def testFieldSpec(self):
        """Reproduce original spec of the field"""
        a = DBStrings._UnfoundField('key')
        b = a['keyname']
        c = b.attribute
        d = c[0]
        a.conversion = 's'
        self.assertEqual("{key['keyname'].attribute[0]!s:04d}",
                         a.field_spec('04d'))


if __name__ == '__main__':
    unittest.main()
