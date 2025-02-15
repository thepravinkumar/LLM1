import os

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    return "File not found"

def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
