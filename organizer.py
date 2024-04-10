from user import User

class Organizer(User):
    def __init__(self, user_id, name, email, company):
        super().__init__(user_id, name, email)
        self.company = company

    def create_event(self, event):
        print(f"Event '{event.name}' created by {self.name} from {self.company}.")

    def delete_event(self, event):
        print(f"Event '{event.name}' deleted by {self.name} from {self.company}.")
