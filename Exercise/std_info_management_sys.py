#Excercise
print("Class Excercise")

#Initializing empty lists and dictionary
students_list = []
students_dict = {}

while True: # while loop ghi dhi continues unless its false
    name = input("Enter students's name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    age = int(input("enter your age: "))
    grade = int(input("enter your grade: "))

# Adding student information to lists and dictionary
students_list.append(name)
students_dict[name] = {'age': age, 'grade' : grade}

print("Student details: ")
for name, info in students_dict.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    
# Searching for student's name
search_name = input("Enter the student's name to search: ")
if search_name in students_dict:
    print("\nStudent found!")
    print(f"Name: {search_name}, Age: {students_dict[search_name]['age']}, Grade: {students_dict[search_name]['grade']}")
else:
    print("Student not found!")

# Removing the student's name
remove_name = input("Enter student name to removed: ") 
if remove_name in students_list:
    students_list.remove(remove_name)
    del students_dict[remove_name]
    print("Name removed successfully!")
else:
    print("Student not found")