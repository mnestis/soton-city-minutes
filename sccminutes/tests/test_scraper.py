
from unittest import TestCase

import sccminutes.scraper as sc


class TestCommitteeList(TestCase):

    def test_returns_list(self):
        comm_list = sc._fetch_list_of_committees()
        self.assertIsInstance(comm_list, list)

    def test_list_not_empty(self):
        comm_list = sc._fetch_list_of_committees()
        self.assertNotEqual(len(comm_list), 0)

    def test_all_items_have_two_elements(self):
        comm_list = sc._fetch_list_of_committees()
        for comm in comm_list:
            self.assertEqual(len(comm), 2)
