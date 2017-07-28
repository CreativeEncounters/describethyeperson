class person:
    
    #Catergories of the Person
    def __init__(self, name, age, gender, hairlength, eyecolour, haircolour, expression):
        self.name = name
        self.age = age
        self.gender = gender
        self.hairlength = hairlength
        self.eyecolour = eyecolour
        self.haircolour = haircolour
        self.expression = expression

    def show(self):
        print self.name

#Need to learn about files

# list of people
people = []

# what word do I put infront of '.txt'
pfile = open('people.txt')

lines = pfile.read().split("\n")

for record in lines:
    data = record.split(',')

    if len(data) < 7:
        break

people.append(stranger(data[0], data[1], data[2]))

for person in people:
    person.show()

while True:
    
    print "Hello, welcome to Describe that Person!"
    print "As the computer describes your person using simple looks of the head."

    print"First question!"
    name = raw_input("What is their name?:")

    print "Second question!"
    age = int(raw_input("What is their age?:"))

    print "Third question!"
    gender = raw_input("What is their Gender?:")
    
    print "Fourth question!"
    hairlength = raw_input("Is the length of their hair short, medium or long?:")

    print "Fifth question!"
    eyecolour = raw_input("Is the eye colour red,orange,yellow,green,blue,purple,blonde,brunette,grey,brown or black?:")

    print "Sixth question!"
    haircolour = raw_input("Is the hair colour red,orange,yellow,green,blue,purple,blonde,brunette,grey,brown or black?:")

    print "Seventh question!"
    expression = raw_input("Is the person always happy,sad,mad,depressed,goofy,crazy or no expression?:")

    stranger = person(name, age, gender, hairlength, eyecolour, haircolour, expression)
    people.append(stranger)

    stop = raw_input("add another person?")
    if stop == 'no':
        break










