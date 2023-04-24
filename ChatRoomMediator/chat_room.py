from person import Person

class ChatRoom:
    def __init__(self) -> None:
        self.peoples: list[Person] = []

    def join(self, person: Person):
        person.chat_room = self
        self.broadcast("Room",person.name + " Join the chat")
        self.peoples.append(person)
        
    def broadcast(self, source: str, message: str) -> None:
        for person in self.peoples:
            if person.name != source:
                person.receive(source, message)
            
    def message(self, source, destination: str, message: str) -> None:
        for person in self.peoples:
            if person.name == destination:
                person.receive(source, message)