# Read a text file and print its content
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

# Example usage
read_text_file('example.txt')

#2
# Write text to a .txt file using an InputStream
def write_text_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

# Example usage
text_to_write = "Hello, this is a test."
write_text_to_file('output.txt', text_to_write)


#3
# Read a file stream and print its content
def read_file_stream(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        print(content)

# Example usage
read_file_stream('example.txt')



#4
# Read a file stream with random access
def read_file_stream_random_access(file_path):
    with open(file_path, 'rb') as file:
        file.seek(0)  # Move to the start of the file
        content = file.read()
        print(content)

# Example usage
read_file_stream_random_access('example.txt')


#5
# Read a file and jump to a particular index using seek()
def read_file_with_seek(file_path, position):
    with open(file_path, 'rb') as file:
        file.seek(position)
        content = file.read()
        print(content)

# Example usage
read_file_with_seek('example.txt', 10)  # Jump to the 10th byte


#6import os

# Check if a file has read and write permissions
def check_file_permissions(file_path):
    read_permission = os.access(file_path, os.R_OK)
    write_permission = os.access(file_path, os.W_OK)
    
    print(f"Read permission: {read_permission}")
    print(f"Write permission: {write_permission}")

# Example usage
check_file_permissions('example.txt')
