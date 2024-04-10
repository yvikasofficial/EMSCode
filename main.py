# main.py

from user import User
from organizer import Organizer
from attendee import Attendee
from event import Event
from venue import Venue
from ticket import Ticket

class EventManagementSystem:
    def __init__(self):
        self.events = []
        self.organizers = []
        self.attendees = []
        self.venues = []

    def create_event(self):
        print("\n=== Create Event ===")
        name = input("Enter event name: ")
        description = input("Enter event description: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        location = input("Enter event location: ")
        event_id = len(self.events) + 1
        event = Event(event_id, name, description, start_date, end_date, location)
        self.events.append(event)
        print(f"Event '{name}' created successfully.")

    def create_organizer(self):
        print("\n=== Create Organizer ===")
        name = input("Enter organizer name: ")
        email = input("Enter organizer email: ")
        company = input("Enter organizer company: ")
        user_id = len(self.organizers) + 1
        organizer = Organizer(user_id, name, email, company)
        self.organizers.append(organizer)
        print(f"Organizer '{name}' from '{company}' created successfully.")

    def create_attendee(self):
        print("\n=== Create Attendee ===")
        name = input("Enter attendee name: ")
        email = input("Enter attendee email: ")
        user_id = len(self.attendees) + 1
        attendee = Attendee(user_id, name, email)
        self.attendees.append(attendee)
        print(f"Attendee '{name}' created successfully.")

    def book_venue(self):
        print("\n=== Book Venue ===")
        name = input("Enter venue name: ")
        capacity = input("Enter venue capacity: ")
        venue_id = len(self.venues) + 1
        venue = Venue(venue_id, name, capacity)
        self.venues.append(venue)
        print(f"Venue '{name}' with capacity '{capacity}' booked successfully.")

    def list_events(self):
        print("\n=== Events ===")
        if not self.events:
            print("No events available.")
        else:
            for event in self.events:
                print(f"Event ID: {event.event_id}, Name: {event.name}, Description: {event.description}")

    def menu(self):
        while True:
            print("\n=== Main Menu ===")
            print("1. Create Event")
            print("2. Create Organizer")
            print("3. Create Attendee")
            print("4. Book Venue")
            print("5. List Events")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_event()
            elif choice == '2':
                self.create_organizer()
            elif choice == '3':
                self.create_attendee()
            elif choice == '4':
                self.book_venue()
            elif choice == '5':
                self.list_events()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = EventManagementSystem()
    app.menu()
