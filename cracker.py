import os
import pyzipper

# Path to the directory containing the password files
passwords_dir = 'passwords'

# Loop over the files in the directory and try each password
file_extracted = False  # Initialize flag variable
for filename in os.listdir(passwords_dir):
    if file_extracted:
        break  # Break out of the loop if file is already extracted
    password_file = os.path.join(passwords_dir, filename)
    with open(password_file, 'r') as f:
        password_lines = f.readlines()
    for password in password_lines:
        password = password.strip()  # Remove any leading/trailing whitespace
        try:
            with pyzipper.AESZipFile('passwords1.zip', 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as extracted_zip:
                extracted_zip.extractall(pwd=str.encode(password))
            print(f'Successfully extracted with password: {password}')
            file_extracted = True  # Set flag variable to True if file is successfully extracted
            break  # Stop trying passwords once the correct one is found
        except Exception as e:
            print(f'Incorrect password: {password}')
