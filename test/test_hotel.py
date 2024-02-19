"""
Tests for the Hotel class in a JSON-based storage system.
This module contains unittests for testing functionalities of
the Hotel class.
"""

import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO

# Ajuste del sys.path para incluir el directorio src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "..", "src")))

# pylint: disable=import-error, wrong-import-position
from hotel import Hotel  # noqa: E402


class TestHotel(unittest.TestCase):
    """Clase de pruebas para la clase Hotel."""

    def setUp(self):
        """Preparación antes de cada prueba."""
        self.hotel = Hotel("Test Hotel", "Test Location")
        if os.path.exists(self.hotel.filename):
            os.remove(self.hotel.filename)

    def test_create_hotel(self):
        """Prueba la creación de un hotel."""
        self.hotel.create_hotel()
        self.assertTrue(os.path.exists(self.hotel.filename))

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel."""
        self.hotel.create_hotel()
        self.hotel.delete_hotel()
        self.assertFalse(os.path.exists(self.hotel.filename))

    def test_display_and_modify_hotel_info(self):
        """Prueba la visualización y modificación de la información del hotel."""
        self.hotel.create_hotel()
        new_info = {'location': 'New Location', 'name': 'New Test Hotel'}
        self.hotel.modify_hotel_info(new_info)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.hotel.display_hotel_info()
            self.assertIn('New Test Hotel', fake_out.getvalue())
            self.assertIn('New Location', fake_out.getvalue())

    def test_reserve_and_cancel_room_success(self):
        """Prueba la reserva y cancelación exitosas de una habitación."""
        self.hotel.create_hotel()
        self.hotel.add_room('001')
        self.hotel.reserve_room('001', 'C001')
        self.hotel.cancel_reservation('001', 'C001')

    def test_reserve_room_failure(self):
        """Prueba el fallo al reservar una habitación."""
        self.hotel.create_hotel()
        with self.assertRaises(Exception):
            self.hotel.reserve_room('002', 'C002')

    def test_cancel_reservation_failure(self):
        """Prueba el fallo al cancelar una reserva."""
        self.hotel.create_hotel()
        with self.assertRaises(Exception):
            self.hotel.cancel_reservation('003', 'C003')

    def tearDown(self):
        """Limpieza después de cada prueba."""
        if os.path.exists(self.hotel.filename):
            os.remove(self.hotel.filename)

if __name__ == '__main__':
    unittest.main()