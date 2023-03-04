import os
import time
import PySimpleGUI as Sg
from src import functions


class TodoWindow:
    def __init__(self):
        if not os.path.exists("todos.txt"):
            with open("todos.txt", "w") as f:
                pass

        self.window = Sg.Window("Todo app",
                                layout=self.__class__._layout(),
                                font=("Helvetiva", 16))

    @staticmethod
    def _layout():
        Sg.theme("Black")
        clock = Sg.Text("", key="clock")
        label = Sg.Text("Type in a todo")
        input_box = Sg.InputText(tooltip="Enter todo", key="todo")
        add_button = Sg.Button("Add")
        list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                              enable_events=True, size=(45, 10))
        edit_button = Sg.Button("Edit")
        complete_button = Sg.Button("Complete")
        exit_button = Sg.Button("Exit")

        return [[clock],
                [label],
                [input_box, add_button],
                [list_box, edit_button, complete_button],
                [exit_button]]

    def process_user_input(self):
        while True:
            event, values = self.window.read(timeout=200)
            self.window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
            match event:
                case "Add":
                    self._add_todo(values["todo"])
                case "Edit":
                    try:
                        self._edit_todo(values["todos"][0], values["todo"])
                    except IndexError:
                        Sg.popup("Please select an item first.", font=("Helvetiva", 20))
                case "Complete":
                    try:
                        self._complete_todo(values["todos"][0])
                    except IndexError:
                        Sg.popup("Please select an item first.", font=("Helvetiva", 16))
                case "todos":
                    self._set_value(values["todos"][0])
                case "Exit" | Sg.WIN_CLOSED:
                    break

        self.window.close()

    def _add_todo(self, new_todo):
        if not new_todo:
            return
        todos = functions.get_todos()
        todos.append(new_todo + "\n")
        functions.write_todos(todos)
        self.window["todos"].update(values=todos)

    def _edit_todo(self, todo_to_edit, new_todo):
        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo + "\n"
        functions.write_todos(todos)
        self.window["todos"].update(values=todos)

    def _complete_todo(self, todo_to_complete):
        todos = functions.get_todos()
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        self.window["todos"].update(values=todos)
        self.window["todo"].update(value="")

    def _set_value(self, value):
        self.window["todo"].update(value=value)


if __name__ == "__main__":
    handler = TodoWindow()
    handler.process_user_input()
