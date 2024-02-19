"""
Tests for the Reservation class in a JSON-based storage system.
This module contains unittests for testing functionalities of
the Reservation class.
"""

import os
import sys
import unittest

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, SRC_DIR)

from reservation import Reservation


class TestReservation(unittest.TestCase):
    """Test cases for the Reservation class."""

    def setUp(self):
        """Preparation before each test."""
        self.reservation_details = {
            'reservation_id': "R001",
            'customer_id': "C001",
            'hotel_name': "Test Hotel",
            'check_in_date': "2023-01-01",
            'check_out_date': "2023-01-05"
        }
        self.reservation = Reservation()
        self.filename = self.reservation.filename
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_create_and_cancel_reservation(self):
        """Test the creation and cancellation of a reservation."""
        self.reservation.create_reservation(self.reservation_details)
        reservations = self.reservation.load_reservations()
        self.assertTrue(
            any((res['reservation_id'] == self.reservation_details
                 ['reservation_id'])
                for res in reservations)
        )

        self.reservation.cancel_reservation(
            self.reservation_details['reservation_id'])
        reservations = self.reservation.load_reservations()
        self.assertFalse(
            any((res['reservation_id'] == self.reservation_details
                 ['reservation_id'])
                for res in reservations)
        )

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.filename):
            os.remove(self.filename)


if __name__ == '__main__':
    unittest.main()
