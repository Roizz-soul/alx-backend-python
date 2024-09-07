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


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for integrated testing """

    @classmethod
    def setUpClass(cls) -> None:
        """ Setup class Function """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url: str):
            """ Payload side effect """
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """ TearDown Function """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
