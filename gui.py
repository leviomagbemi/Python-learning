import functions
import PySimpleGUI as sg

label = sg.Text("Add a Todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window("Todo App",
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button]],
                   font=("Poppins", 18))

while True:
    event, value = window.read()
    print(event)
    print(value)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value='')

        case 'Edit':
            todos_to_edit = value["todos"][0]
            new_todo = value["todo"] + "\n"

            todos = functions.get_todos()
            index = todos.index(todos_to_edit)

            todos[index] = new_todo
            functions.write_todos(todos)

            window["todos"].update(values=todos)
            window["todo"].update(value='')

        case "todos":
            window["todo"].update(value=value["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()
