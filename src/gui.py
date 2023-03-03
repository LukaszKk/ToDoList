import PySimpleGUI as Sg
from src import functions


if __name__ == "__main__":
    label = Sg.Text("Type in a todo")
    input_box = Sg.InputText(tooltip="Enter todo", key="todo")
    add_button = Sg.Button("Add")
    list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                          enable_events=True, size=(45, 10))
    edit_button = Sg.Button("Edit")

    window = Sg.Window("Todo app",
                       layout=[[label], [input_box, add_button], [list_box, edit_button]],
                       font=("Helvetiva", 20))

    while True:
        event, values = window.read()
        print(event)
        print(values)
        match event:
            case "Add":
                if not values["todo"]:
                    continue
                todos = functions.get_todos()
                new_todos = values["todo"] + "\n"
                todos.append(new_todos)
                functions.write_todos(todos)
            case "Edit":
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            case Sg.WIN_CLOSED:
                break

    window.close()
