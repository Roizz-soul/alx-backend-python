#!/usr/bin/env python3
""" Test module for utils """
from client import GithubOrgClient
from parameterized import parameterized
from typing import Mapping, Sequence, Dict
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test GithubOrgClient """
    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, a: str, res: Dict, mock_get: Mock) -> None:
        """ Function to test org """
        mock_get.return_value = res
        result = GithubOrgClient(a)
        self.assertEqual(result.org, res)
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{a}")
