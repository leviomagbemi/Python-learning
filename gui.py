import functions
import PySimpleGUI as sg
import time

sg.theme("black")

clock = sg.Text(key="clock")
label = sg.Text("Add a Todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")


layout = [
    [clock],
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
         ]

window = sg.Window("Todo App", layout=layout, font=("Poppins", 18))

while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value='')

        case 'Edit':
            try:
                todos_to_edit = value["todos"][0]
                new_todo = value["todo"] + "\n"

                todos = functions.get_todos()
                index = todos.index(todos_to_edit)

                todos[index] = new_todo
                functions.write_todos(todos)

                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except Exception as e:
                print('Error: ', e)
                sg.popup("Please select a todo first", font=("Poppins", 18))

        case "Complete":
            try:
                complete_todo = value["todos"][0]
                todos = functions.get_todos()

                index = todos.remove(complete_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except Exception as e:
                print("error: ", e)
                sg.popup("Please select a todo first", font=("Poppins", 18))
        case "Exit":
            break

        case "todos":
            window["todo"].update(value=value["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()
