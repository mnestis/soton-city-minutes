
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

    def test_returned_items_are_int_and_str(self):
        comm_list = sc._fetch_list_of_committees()
        for comm_id, comm_name in comm_list:
            self.assertIsInstance(comm_id, int)
            try:
                self.assertIsInstance(comm_name,  unicode)
            except NameError:
                self.assertIsInstance(comm_name, str)


class TestMeetingList(TestCase):

    def setUp(self):
        comm_list = sc._fetch_list_of_committees()
        self.council_id = [comm_id
                           for comm_id, comm_name
                           in comm_list
                           if comm_name == "Council"][0]

    def test_returns_list(self):
        meet_list = sc._fetch_list_of_meetings(self.council_id)
        self.assertIsInstance(meet_list, list)

    def test_list_not_empty(self):
        meet_list = sc._fetch_list_of_meetings(self.council_id)
        self.assertNotEqual(len(meet_list), 0)

    def test_all_items_have_four_elements(self):
        meet_list = sc._fetch_list_of_meetings(self.council_id)
        for meet in meet_list:
            self.assertEqual(len(meet), 4)

    def test_all_items_have_right_meet_id(self):
        meet_list = sc._fetch_list_of_meetings(self.council_id)
        for meet in meet_list:
            self.assertEqual(meet[0], self.council_id)

    def test_returned_items_are_ints_and_str(self):
        meet_list = sc._fetch_list_of_meetings(self.council_id)
        for comm_id, meet_id, ver, meet_time in meet_list:
            self.assertIsInstance(comm_id, int)
            self.assertIsInstance(meet_id, int)
            self.assertIsInstance(ver, int)
            try:
                self.assertIsInstance(meet_time, unicode)
            except NameError:
                self.assertIsInstance(meet_time, str)
