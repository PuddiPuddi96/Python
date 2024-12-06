from random import randint
from pandas import DataFrame

# Comprehension for a list
numbers = [1, 2, 3]
new_numbers_list = [n + 1 for n in numbers]
print(new_numbers_list)

# Comprehension for a String
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

# Comprehension for a range
range_list = [number * 2 for number in range(1, 5)]
print(range_list)

# Comprehension for a list with a condition
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", 'Freddie']
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 4]
print(short_names)
print(long_names)

# Comprehension to create a dictionary
# new_dictionary = {new_key:new_value for item in a_list if test}
students_score = {student:randint(0, 100) for student in names}
print(students_score)

# new_dictionary = {new_key:new_value for (key,value) in a_dictionary.items() if test}
passed_students = {student:score for (student,score) in students_score.items() if score > 60}
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key, value)

student_data_frame = DataFrame(student_dict)
print(student_data_frame)

# Looping through data frame
# for (key, value) in student_data_frame.items():
#     print(key, value)

for (index, row) in student_data_frame.iterrows():
    print(row) # Print row
    print(row.student) # Print row for a specific column
    if row.student == "Angela": # Print with a condition
        print(row.score)
