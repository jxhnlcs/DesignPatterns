from person import Person
from responsible_person import ResponsiblePerson

responsible_person = ResponsiblePerson(Person(26))
print(responsible_person.check_if_drinking())
print(responsible_person.check_if_driving())
print(responsible_person.check_if_drinking_and_driving())