FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Open and read a text file and return a list of items inside the file."""
    with open(filepath, 'r') as file_local: #open a file in the read mode
        todos_local = file_local.readlines()  #read the file content and return a list
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ Open and read a text file and write a new list of items inside the file."""
    with open(filepath, 'w') as file_local:  # open the file in the write mode
        file_local.writelines(todos_arg)  # override the content in the text file with the new content from the above step
