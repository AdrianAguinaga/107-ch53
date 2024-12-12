# example of variable
# let name = variable;  JS var = variable
name = "Adrian"  # string 
age = 38 #integer
height = 1.86 #float
is_student = False # boolean


print (f"Name: {name}, age: {age}, height: {height}")
print ("Type of age: ", type(name))

#Example of an if statement
age = 15 #integer
if age < 13:
    print ("Child")
elif age < 20:
    print ("Teenager")
else:
    print ("Adult")
    
# for loops
for numbers in range(5):
    print(numbers)

# List --> array
fruits = ["Apple", "banana", "cherry"]
print(fruits)
fruits.append("date")
print(fruits)
print (fruits[1:3])

# dictionary
student = {
    "name": "Adrian",
    "age": 20,
    "cousers": ["math","sciences"]
}
print(student["age"])
student["grade"] = "A"
student.update({"email":"arodriguez@sd.com"})
print(student)

# fuctions
def say_hello():
    print("Hello")

def say_goodbye():
    print("Goodbye")
#call the functions
say_hello()
say_goodbye()

# concatenate
print("Hello my name is " + name + " and i have "+ str(age) + " old")

