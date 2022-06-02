import csv
from classes.person import Person

class Student(Person):
  
    def all_students():
        student = []
        with open('/Users/radd_c/Downloads/CPlatoon/exercises/oop-school-interface-i/data/students.csv') as s:
            read = csv.DictReader(s)

            for row in read:
                student.append(row)

            return student

