from user import User

class Attendee(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.registered_events = []

    def register_for_event(self, event):
        self.registered_events.append(event)
        print(f"{self.name} registered for the event '{event.name}'.")

    def cancel_registration(self, event):
        self.registered_events.remove(event)
        print(f"{self.name} canceled registration for the event '{event.name}'.")
