import os

directory = '/home/pragya/python-project/task-automation'

# Rename multiple .txt files
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        new_name = filename.replace('.txt', '_renamed.txt')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Files renamed successfully.")



 