"""
Module for managing reservations in a JSON-based storage system.
Provides functionalities to create and cancel reservations.
"""


import json
import os


class Reservation:
    """Class representing a reservation management system."""

    def __init__(self):
        """Initialize a new Reservation instance."""
        self.filename = "reservations.json"

    def load_reservations(self):
        """Load reservations from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_reservations(self, reservations):
        """Save reservations to a JSON file."""
        with open(
            self.filename, 'w', encoding='utf-8'
        ) as f:
            json.dump(reservations, f, indent=4)

    def create_reservation(self, reservation_details):
        """Create new reservation and add it to the JSON file."""
        reservations = self.load_reservations()
        reservation_id = reservation_details['reservation_id']

        if any(
            res['reservation_id'] == reservation_id
            for res in reservations
        ):
            print("Reservation ID already exists.")
            return

        reservations.append(reservation_details)
        self.save_reservations(reservations)
        print(
            f"Reservation {reservation_id} created",
            end=" "
        )
        print("successfully.")

    def cancel_reservation(self, reservation_id):
        """Cancel an existing reservation."""
        reservations = self.load_reservations()
        reservation_to_cancel = next(
            (
                res for res in reservations
                if res['reservation_id'] == reservation_id
            ), None
        )

        if reservation_to_cancel:
            reservations.remove(reservation_to_cancel)
            self.save_reservations(reservations)
            print(
                f"Reservation {reservation_id} canceled",
                end=" "
            )
            print("successfully.")
        else:
            print("Reservation ID does not exist.")
