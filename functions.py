FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list
    of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local):
    """ Write a to-do items in the text file. """
    with open(FILEPATH, 'w') as file_local:
        file_local.writelines(todos_local)


if __name__ == "__main__":
    print('hello from functions')
