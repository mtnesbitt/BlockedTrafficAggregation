from unittest import TestCase
from mock_blocked_traffic_api import MockBlockedTrafficAPI

class TestMockBlockedTrafficAPI(TestCase):

    def test_get_one_address(self):
        mock = MockBlockedTrafficAPI(1)
        self.assertEquals(mock.get_addresses(),["9.9.9.9"])

    def test_get_multiple_addresses(self):
        mock = MockBlockedTrafficAPI(5)
        self.assertEquals(mock.get_addresses(),["9.9.9.9",
        "8.8.8.8", "7.7.7.7", "6.6.6.6", "5.5.5.5"])

    def test_get_all_addresses(self):
        mock = MockBlockedTrafficAPI(10)
        self.assertEquals(mock.get_addresses(),["9.9.9.9",
        "8.8.8.8", "7.7.7.7", "6.6.6.6", "5.5.5.5", "4.4.4.4", "3.3.3.3",
        "2.2.2.2", "1.1.1.1", "0.0.0.0"])