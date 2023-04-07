import os
import shutil

# Get the ID to search for
id_to_search = input("Enter the ID to search for: ")

# Get the absolute path of the current script file
current_script_path = os.path.abspath(__file__)

# Get the directory containing the script file
current_dir = os.path.dirname(current_script_path)

# Change the current working directory to the script directory
os.chdir(current_dir)

# Create a subdirectory with the input ID as the name
sub_dir = os.path.join(current_dir, id_to_search)
os.mkdir(sub_dir)

# Search for files containing the input ID and move them to the subdirectory
for file_name in os.listdir(current_dir):
    if file_name.endswith('.txt'):  # change the extension as needed
        if id_to_search in file_name:
            file_path = os.path.join(current_dir, file_name)
            shutil.move(file_path, sub_dir)
            
print("Search and move completed successfully!")
