from person import Person


class ResponsiblePerson:
    def __init__(self, person: Person):
        self.person = person

    def check_if_drinking(self)-> str:
        return self.person.drinking() if self.person.age >= 18 else "very young"
    
    def check_if_driving(self) -> str:
        return self.person.driving() if self.person.age >= 16 else "very young"

    def check_if_drinking_and_driving(self)-> str:
        if self.check_if_drinking() == "drinking" and self.person.driving() == "driving":
            return self.person.drinking_and_driving() + ", u are dead"
        else:
            return "u can drive in piece my friend"

