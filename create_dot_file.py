import csv
import sys
import hashlib

def hash(text):
	return hashlib.sha1(bytes(text, "utf-8")).hexdigest()

class Person:

	def __init__(self, row):
		self.row = row
		
		self.name = self.row[0]
	
	@property
	def id(self):
		return hash(self.name)
		
	def should_display(self):
		return True

def main(contacts, output):
	persons = [Person(row) for row in csv.reader(contacts)][1:]
	
	output.write("diagraph G {\n")
	
	for person in filter(lambda p: p.should_display(), persons):
		output.write("%s[label='%s'];\n" % (person.id, person.name))
	
	output.write("}\n")

if __name__ == "__main__":
	with open(sys.argv[1], "r") as contacts, open(sys.argv[2], "w") as output_dot_file:
		main(contacts, output_dot_file)
