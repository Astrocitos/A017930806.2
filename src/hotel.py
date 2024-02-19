"""Module for managing hotel information and reservations using a JSON storage
system."""

import json
import os


class Hotel:
    """Represents a hotel, managing its information and reservations."""

    def __init__(self, name, location):
        """Initialize a new Hotel instance with name, location, and
        filename for JSON storage."""
        self.name = name
        self.location = location
        self.filename = f"{name.replace(' ', '_').lower()}.json"

    def hotel_exists(self):
        """Check if the hotel's JSON data file exists."""
        return os.path.exists(self.filename)

    def save_to_file(self, data):
        """Save hotel data to a JSON file with UTF-8 encoding."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        """Load hotel data from a JSON file if it exists."""
        if self.hotel_exists():
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def create_hotel(self):
        """Create hotel data and save it to a JSON file if it does not
        already exist."""
        if self.hotel_exists():
            print("Hotel already exists.")
            return
        hotel_data = {
            'name': self.name,
            'location': self.location,
            'rooms': [],
            'reservations': []
        }
        self.save_to_file(hotel_data)
        print(f"Hotel '{self.name}' created successfully.")

    def delete_hotel(self):
        """Delete the hotel's JSON data file if it exists."""
        if self.hotel_exists():
            os.remove(self.filename)
            print(f"Hotel '{self.name}' deleted successfully.")
        else:
            print("Hotel does not exist.")

    def display_hotel_info(self):
        """Display information about the hotel, including rooms and
        reservations."""
        if self.hotel_exists():
            hotel_data = self.load_from_file()
            print(f"Hotel Name: {hotel_data['name']}\n"
                  f"Location: {hotel_data['location']}\n"
                  f"Rooms: {len(hotel_data['rooms'])}\n"
                  f"Reservations: {len(hotel_data['reservations'])}")
        else:
            print("Hotel does not exist.")

    def modify_hotel_info(self, new_info):
        """Update the hotel's information with new data provided in
        new_info dictionary."""
        if not self.hotel_exists():
            print("Hotel does not exist.")
            return
        hotel_data = self.load_from_file()
        hotel_data.update(new_info)
        self.save_to_file(hotel_data)
        print(f"Hotel '{self.name}' updated successfully.")

    def add_room(self, room_id):
        """Agregar una nueva habitación al hotel."""
        if not self.hotel_exists():
            raise Exception("Hotel does not exist.")
        
        hotel_data = self.load_from_file()
        hotel_data['rooms'].append({'id': room_id, 'reserved': False})
        self.save_to_file(hotel_data)
        print(f"Room {room_id} added successfully.")
    
    def reserve_room(self, room_id, customer_id):
        """Reserve a room for a customer by updating the room's
        reservation status."""
        if not self.hotel_exists():
            raise Exception("Hotel does not exist.")
        
        hotel_data = self.load_from_file()
        room_found = False
        for room in hotel_data['rooms']:
            if room['id'] == room_id:
                room_found = True
                if room.get('reserved'):
                    raise Exception("Room not available or already reserved.")
                room['reserved'] = True
                hotel_data['reservations'].append(
                    {'room_id': room_id, 'customer_id': customer_id})
                self.save_to_file(hotel_data)
                print(f"Room {room_id} reserved successfully.")
                break
        
        if not room_found:
            raise Exception("Room does not exist.")

    def cancel_reservation(self, room_id, customer_id):
        """Cancel a room reservation for a customer."""
        if not self.hotel_exists():
            raise Exception("Hotel does not exist.")
        
        hotel_data = self.load_from_file()
        for reservation in hotel_data['reservations']:
            if (reservation['room_id'] == room_id and
                    reservation['customer_id'] == customer_id):
                hotel_data['reservations'].remove(reservation)
                for room in hotel_data['rooms']:
                    if room['id'] == room_id:
                        room['reserved'] = False
                self.save_to_file(hotel_data)
                print(f"Reservation for room {room_id} canceled successfully.")
                return
        raise Exception("Reservation does not exist.")
