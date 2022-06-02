import csv
from classes.person import Person

class Staff(Person):
  
    def all_staff():
        staff = []
        with open('/Users/radd_c/Downloads/CPlatoon/exercises/oop-school-interface-i/data/staff.csv') as s:
            read = csv.DictReader(s)

            for row in read:
                staff.append(row)

            return staff