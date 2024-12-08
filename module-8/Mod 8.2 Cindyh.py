#Cindy Hernandez
#12/9/24
#mod 8.2

import json
import subprocess  # For system notifications

# Path to the student.json file
file_path = 'student.json'

# Function to print the student list
def print_student_list(students):
    for student in students:
        print(f"{student['F_Name']} {student['L_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

# Load the existing students from the JSON file
with open(file_path, 'r') as file:
    student_list = json.load(file)

# Output notification that this is the original student list
print("Original Student List:")
print_student_list(student_list)  # Print only once here

# Add new student (your information)
new_student = {
    "F_Name": "Cindy",            # First name
    "L_Name": "Hernandez",        # Last name
    "Student_ID": "01271545",     # Fictional ID
    "Email": "cihernandez@my365.bellevue.edu"  # My Email
}

# Append the new student to the list
student_list.append(new_student)

# Output notification that this is the updated student list
print("\nUpdated Student List:")
print_student_list(student_list)  # Print only once here

# Ask the user whether they want to save the updated list
user_choice = input("\nDo you want to save the updated student list to student.json? (yes/no): ").strip().lower()

# Handle the user's choice
if user_choice == 'yes':
    # Save the updated student list back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(student_list, file, indent=4)
    
    # Output notification that the JSON file has been updated
    print("\nThe student.json file has been updated successfully.")
    
    # Trigger a system-level notification that the file has been updated
    subprocess.run(['notify-send', 'File Update', 'The student.json file has been updated successfully.'])

else:
    print("\nThe changes have not been saved. student.json remains unchanged.")
    
    # Trigger a system-level notification indicating that the changes were not saved
    subprocess.run(['notify-send', 'File Update', 'The changes were not saved. student.json remains unchanged.'])
