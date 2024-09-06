#!/usr/bin/env python3
""" Test module for utils """
from parameterized import parameterized
from typing import Mapping, Sequence, Dict
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Class to test access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, a: Mapping, b: Sequence, e) -> None:
        """ Fuction for the test on access nested map"""
        self.assertEqual(access_nested_map(a, b), e)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(
        self, a: Mapping, b: Sequence, r: str
    ) -> None:
        """ Tests for exceptions raised """
        with self.assertRaises(KeyError) as e:
            access_nested_map(a, b)
        self.assertEqual(str(e.exception), f"'{r}'")


class TestGetJson(unittest.TestCase):
    """ Class to test get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, a: str, b: Dict) -> None:
        """ Funtion to test get json """
        with patch("requests.get") as req:
            mock = Mock()
            mock.json.return_value = b
            req.return_value = mock
            result = get_json(a)

            req.assert_called_once_with(a)
            self.assertEqual(result, b)
        


class TestMemoize(unittest.TestCase):
    """ Class to test Memoize """
    def test_memoize(self):
        """ Function to test memoize """
        class TestClass:
            """ Test Class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as meth:
            myClass = TestClass()
            res1 = myClass.a_property
            res2 = myClass.a_property
            
            meth.assert_called_once()

            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)


if __name__ == '__main__':
    unittest.main()
