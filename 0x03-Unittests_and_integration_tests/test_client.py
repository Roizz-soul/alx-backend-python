#!/usr/bin/env python3
""" Test module for utils """
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get: Mock):
        """ Function to test public repos """
        payload = [{"name": "www"}]
        mock_get.return_value = payload
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mick:
            mick.return_value = "www"
            res = GithubOrgClient("www")
            self.assertEqual(res.public_repos(None), ["www"])
            mock_get.assert_called_once()
            mick.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, a: Dict[str, Dict], b: str, c: bool):
        """ Function to test has_license """
        res = GithubOrgClient("www")
        self.assertEqual(res.has_license(a, b), c)


@parameterized_class(("a", "b", "c", "d"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for integrated testing """

    @classmethod
    def setUpClass(cls):
        """ Setup Function """
        route_payload = {
            'https://api.github.com/orgs/google': cls.a,
            'https://api.github.com/orgs/google/repos': cls.b,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """ Test public repo"""
        res = GithubOrgClient("google")
        self.assertEqual(res.public_repos(), self.c)

    def test_public_repos_with_license(self):
        """Test public repos with license"""
        res = GithubOrgClient("google")
        self.assertEqual(res.public_repos(license="apache-2.0"), self.d)

    @classmethod
    def tearDownClass(cls):
        """ TearDown Function """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
