import csv
import sys
import hashlib

def hash(text):
    result = hashlib.sha1(bytes(text, "utf-8")).hexdigest()

    for number, letter in {
        "0": "g", "1": "h", "2": "i", "3": "j", "4": "k",
        "5": "l", "6": "m", "7": "n", "8": "o", "9": "p"
    }.items():
        result = result.replace(number, letter)

    return result

class Person:

    def __init__(self, row):
        self.row = row
        self.name = self.row[0]
        self.status = self.row[9]
        self.guide = self.row[8]

    @property
    def id(self):
        return hash(self.name)

    def should_display(self):
        return self.status == "aktiv" or (self.status == "" and self.guide)

def main(contacts, output):
    persons = [Person(row) for row in csv.reader(contacts)][1:]

    output.write("digraph G {\n")

    for person in filter(lambda p: p.should_display(), persons):
        output.write("%s[label=\"%s\"];\n" % (person.id, person.name))

        if person.guide:
            output.write("%s -> %s;\n" % (hash(person.guide), person.id))

    output.write("}\n")

if __name__ == "__main__":
    with open(sys.argv[1], "r") as contacts, open(sys.argv[2], "w") as output_dot_file:
        main(contacts, output_dot_file)
