# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f"{index + 1}. {item}")
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            number = int(user_action[5:])
            newTodo = input("Enter a new todo: ") + "\n"
            todos[number - 1] = newTodo

            functions.write_todos(todos)
        except ValueError:
            print("Invalid command")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            completed = int(user_action[9:])
            completedTodos = todos[completed - 1]
            todos.remove(completedTodos)

            functions.write_todos(todos)

            completedTodos = completedTodos.strip("\n")

            print(f"\"{completedTodos}\" removed from todos")
        except IndexError:
            print("There is no todos with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command")

print('bye')
