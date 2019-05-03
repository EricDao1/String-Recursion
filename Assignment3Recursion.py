import unittest

# Recursion Assignment from CS2050 by Dr. Beaty

'''
Write a recursive method that takes 1) a string to find, 2) a string to replace the found string with, and 
3) an initial string. Return the initial string with all the found strings replaced with the replacement string. 
You may not use loops or the built-in string methods except comparison, length, and slicing. Here is an outline.
'''

'''
Description: This program uses recursion to replace all instances of find with replace in a string.
Author: Eric Dao
Version: 3.6
Help received from: 
Help provided to: 
'''


def findandreplace(find, replace, string):
    if string is None:
        return None
    if find is None or find == "" or replace is None:
        return string
    if string == "":
        return ""
    if string[0:len(find)] == find:
        return replace + findandreplace(find, replace, string[len(find):])
    else:
        return string[0] + findandreplace(find, replace, string[1:])

    '''
    Replace all instances of find with replace in string.

    Recursive approach:
    If the string starts with find
        return replace and call findandreplace with the rest of the string
    '''

    '''
    else
        return the first character of the string and call findandreplace with the rest of the string
    '''


class TestFindAndReplace(unittest.TestCase):
    def test_all_none(self):
        self.assertEqual(findandreplace(None, None, None), None)

    def test_find_none(self):
        self.assertEqual(findandreplace(None, "a", "aabb"), "aabb")

    def test_find_empty(self):
        self.assertEqual(findandreplace("", "a", "aabb"), "aabb")

    def test_replace_none(self):
        self.assertEqual(findandreplace("a", None, "aabb"), "aabb")

    def test_string_none(self):
        self.assertEqual(findandreplace("a", "b", None), None)

    def test_simple(self):
        self.assertEqual(findandreplace("a", "b", "aabb"), "bbbb")

    def test_remove(self):
        self.assertEqual(findandreplace(" ", "", " a abb"), "aabb")

    def test_gettysburg(self):
        self.assertEqual(findandreplace("Four score", "Twenty", \
                                        "Four score and seven years ago"), "Twenty and seven years ago")


if __name__ == '__main__':
    unittest.main()
