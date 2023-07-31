# Dictionaries Practice

books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}

print(books["The Handmaiden's Tale"])
# 'Margaret Atwood'

print(books["Margaret Atwood"])
# KeyError: 'Margaret Atwood'
# Because it is a value not a key - dictionaries cannot be queried using a value

# Exercise time yaey

books = {"Kate O\'Hearn":"Pegasus", "Rachel Caine":"Morganville Vampires", "Rick Riordan":"Heroes of Olympus"}

new_book=input("Gimme a name of an author cause my dictionary is smol: ")

books.sort() #this will change the original list so BE CAREFUL
print(new_book + ", " + ", ".join(books))