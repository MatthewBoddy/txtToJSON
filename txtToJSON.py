import json
import os

def get_valid_file(prompt):
    while True:
        file_path = input(prompt)
        if os.path.exists(file_path):
            return file_path
        else:
            print(f"Error: The file '{file_path}' does not exist. Please try again.")

def create_json_from_txt(usernames_file, passwords_file, output_file):
    try:
        with open(usernames_file, 'r') as user_file:
            usernames = [line.strip() for line in user_file.readlines()]
        
        with open(passwords_file, 'r') as pass_file:
            passwords = [line.strip() for line in pass_file.readlines()]
        
        data = {
            "usernames": usernames,
            "passwords": passwords
        }
        
        with open(output_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"\nData successfully written to {output_file}\n")
    
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n")

usernames_txt = get_valid_file("\nEnter the path for the usernames file: ")
passwords_txt = get_valid_file("\nEnter the path for the passwords file: ")
output_json = input("\nEnter the path for the output JSON file: ")

create_json_from_txt(usernames_txt, passwords_txt, output_json)
