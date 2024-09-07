#!/usr/bin/env python3
""" Test module for utils """
from client import GithubOrgClient
from parameterized import parameterized
from typing import Mapping, Sequence, Dict
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch, PropertyMock
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

    def test_public_repos_url(self) -> None:
        """ Function to test public_repos_url """
        payload = {
            "repos_url": "https://api.github.com/orgs/repos_url/repos"}
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_method:
            mock_method.return_value = payload
            res = GithubOrgClient("repos_url")
            self.assertEqual(
                res._public_repos_url,
                "https://api.github.com/orgs/repos_url/repos"
            )
