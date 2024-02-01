# String formatting
letter = ["apple"]
print(letter)

#String Travasal using for loop
fruit = ["banana"]
for char in fruit:
    print(char)

#String travasal using while loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

#String Operation and methods
line="new world"
new_line=line.capitalize()
print(line)
print(new_line)

#Escaping the sequemnce
question=r"He said,""what\'s is your name?"
print(question)

error_no=45678910
name='Sam'
print("Hey {}, there is 0x{:x} error!".format(name,error_no))

