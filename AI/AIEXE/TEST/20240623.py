import os
import random
import subprocess

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
directories = [d for d in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, d))]

if directories:
    random_directory = random.choice(directories)
    # os.startfile(os.path.join(desktop_path, random_directory))
else:
    print("No directories found on the desktop.")

# It seems that the code execution did not produce any visible output in the provided results. This could be due to
# the fact that there were no directories found on the desktop to open randomly. In the context of the code provided,
# the script first identifies all directories on the user's desktop and then randomly selects one of those
# directories to open. If no directories are found on the desktop, it will print a message indicating that no
# directories were found. Since the output is empty, it suggests that there were no directories on the desktop to
# select from or there might be an issue with the code execution. You may want to check if there are directories
# present on your desktop and ensure that the code is executed correctly to verify the functionality.


# GENERATED CODE
# This code is proposed for mission execution Additional code included at the top of this file ensures
# smooth operation. For a more detailed review, it is recommended to open the actual file. Please review the code
# carefully as it may cause unintended system behavior You can modify this code before execute

# Change the directory to the 'git' folder on the desktop
git_folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'git')
os.chdir(git_folder)

# Get the current branch name using Git command
result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
branch_name = result.stdout.decode().strip()

print("Current branch name:", branch_name)

# GENERATED CODE This code is proposed for mission execution Additional code included at the top of this file ensures
# smooth operation. For a more detailed review, it is recommended to open the actual file. Please review the code
# carefully as it may cause unintended system behavior You can modify this code before execute

git_folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'git')
os.chdir(git_folder)

result = subprocess.run(['git', 'remote', 'get-url', 'origin'], stdout=subprocess.PIPE)
repository_url = result.stdout.decode().strip()

repository_name = repository_url.split('/')[-1].replace('.git', '')

print("Repository name:", repository_name)

# GENERATED CODE This code is proposed for mission execution Additional code included at the top of this file ensures
# smooth operation. For a more detailed review, it is recommended to open the actual file. Please review the code
# carefully as it may cause unintended system behavior You can modify this code before execute

# Define the path to the user's desktop git folder
git_folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'git', 'linux')

# Change directory to the git folder
os.chdir(git_folder)

# Get the list of remote repositories
result = subprocess.run(['git', 'remote', '-v'], stdout=subprocess.PIPE)
repositories_info = result.stdout.decode().splitlines()

# Print the information of all GitHub repositories on the computer
print("GitHub repository information on the computer:")
for info in repositories_info:
    print(info)

# Specify the path to the folder containing .md files
folder_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'git', 'ufc', 'Obsidian', 'main', 'Akim',
                           'English')

# Specify the output folder path to save the extracted content
output_folder = r'C:\Users\wowp1\PycharmProjects\python\AI\AIEXE\TEST'

# Check if the folder_path exists
if os.path.exists(folder_path):
    # List files in the folder
    files = os.listdir(folder_path)

    # Iterate through each file in the folder
    for file in files:
        file_path = os.path.join(folder_path, file)
        # Check if the file is a regular file and has .md extension
        if os.path.isfile(file_path) and file.endswith('.md'):
            # Open the output file in write mode
            with open(os.path.join(output_folder, file), 'w', encoding='utf-8') as output_file:
                # Open the current .md file to read its content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Write the content of the .md file to the output file
                    output_file.write(f"Content of {file}:\n")
                    output_file.write(content)
else:
    print("The 'English' folder does not exist in the specified path.")
