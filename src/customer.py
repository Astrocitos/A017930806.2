"""Module for managing customers using a JSON storage system."""

import json
import os


class Customer:
    """Represents a customer for the JSON storage system."""

    def __init__(self, customer_id, name, email):
        """Initialize a new Customer instance."""
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.filename = "customers.json"

    def load_customers(self):
        """Load customers from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_customers(self, customers):
        """Save customers to a JSON file."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(customers, f, indent=4)

    def customer_exists(self, customer_id):
        """Check if a customer exists by their ID."""
        customers = self.load_customers()
        for customer in customers:
            if customer['customer_id'] == customer_id:
                return True, customer
        return False, None

    def create_customer(self):
        """Create a new customer and add them to the JSON file."""
        exists, _ = self.customer_exists(self.customer_id)
        if exists:
            print("Customer already exists.")
            return
        customer_data = {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email
        }
        customers = self.load_customers()
        customers.append(customer_data)
        self.save_customers(customers)
        print(f"Customer '{self.name}' created successfully.")

    def delete_customer(self):
        """Delete a customer by their ID."""
        exists, customer = self.customer_exists(self.customer_id)
        if not exists:
            print("Customer does not exist.")
            return
        customers = self.load_customers()
        customers.remove(customer)
        self.save_customers(customers)
        print(f"Customer '{self.name}' deleted successfully.")

    def display_customer_info(self):
        """Display information for a specific customer."""
        exists, customer = self.customer_exists(self.customer_id)
        if exists:
            print(
                f"Customer ID: {customer['customer_id']}\n"
                f"Name: {customer['name']}\n"
                f"Email: {customer['email']}"
                )
        else:
            print("Customer does not exist.")

    def modify_customer_info(self, new_name=None, new_email=None):
        """Modify the information for an existing customer."""
        exists, customer = self.customer_exists(self.customer_id)
        if not exists:
            print("Customer does not exist.")
            return
        if new_name:
            customer['name'] = new_name
        if new_email:
            customer['email'] = new_email
        customers = self.load_customers()
        for i, c in enumerate(customers):
            if c['customer_id'] == self.customer_id:
                customers[i] = customer
                break
        self.save_customers(customers)
        print(f"Customer '{self.customer_id}' updated successfully.")
