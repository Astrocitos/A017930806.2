"""
Tests for the Customer class in a JSON-based storage system.
This module contains unittests for testing functionalities of
the Customer class.
"""

import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO

# Ajuste del sys.path para incluir el directorio src
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, SRC_DIR)

from customer import Customer  # noqa: E402


class TestCustomer(unittest.TestCase):
    """Test cases for the Customer class."""

    def setUp(self):
        """Initialize resources for testing."""
        self.customer = Customer("001", "Test Customer", "test@example.com")
        if os.path.exists(self.customer.filename):
            os.remove(self.customer.filename)

    def test_create_and_delete_customer(self):
        """Test creation and deletion of a customer."""
        self.customer.create_customer()
        exists, _ = self.customer.customer_exists(self.customer.customer_id)
        self.assertTrue(exists)

        self.customer.delete_customer()
        exists, _ = self.customer.customer_exists(self.customer.customer_id)
        self.assertFalse(exists)

    def test_display_customer_info(self):
        self.customer.create_customer()
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.customer.display_customer_info()
            expected_output = "Customer ID: 001\nName: Test Customer\nEmail: test@example.com\n"
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_modify_customer_info(self):
        self.customer.create_customer()
        self.customer.modify_customer_info(new_name="New Test Customer", new_email="newtest@example.com")
        exists, customer_data = self.customer.customer_exists(self.customer.customer_id)
        self.assertTrue(exists)
        self.assertEqual(customer_data['name'], "New Test Customer")
        self.assertEqual(customer_data['email'], "newtest@example.com")
    
    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.customer.filename):
            os.remove(self.customer.filename)


if __name__ == '__main__':
    unittest.main()
