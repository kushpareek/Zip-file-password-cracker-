import os
import random
import string

# Define the characters to use in the passwords
chars = string.ascii_letters + string.digits

# Define the minimum and maximum length of the passwords
min_length = 8
max_length = 15

# Define the number of files to generate and the number of passwords per file
num_files = 100
num_lines = 100000

# Create a directory to store the password files
os.makedirs('passwords', exist_ok=True)

# Generate multiple password files
all_passwords = set()  # Set to store all passwords generated so far
for i in range(num_files):
    # Open a new password file
    filename = f'passwords/passwords_{i+1}.txt'
    with open(filename, 'w') as file:
        # Generate passwords and write them to the file
        passwords = set()
        while len(passwords) < num_lines:
            password = ''.join(random.choices(chars, k=random.randint(min_length, max_length)))
            if password not in all_passwords:  # Check if password is already in use
                passwords.add(password)
                all_passwords.add(password)
        for password in passwords:
            file.write(password + '\n')
        # Print a message for each file generated
        print(f"Generated file: {filename}")
