import PySimpleGUI as Sg
from src import functions


class TodoWindow:
    def __init__(self):
        self.window = Sg.Window("Todo app",
                                layout=self.__class__._layout(),
                                font=("Helvetiva", 20))

    @staticmethod
    def _layout():
        label = Sg.Text("Type in a todo")
        input_box = Sg.InputText(tooltip="Enter todo", key="todo")
        add_button = Sg.Button("Add")
        list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                              enable_events=True, size=(45, 10))
        edit_button = Sg.Button("Edit")
        return [[label], [input_box, add_button], [list_box, edit_button]]

    def process_user_input(self):
        while True:
            event, values = self.window.read()
            print(event)
            print(values)
            match event:
                case "Add":
                    self._add_todo(values["todo"])
                case "Edit":
                    self._edit_todo(values["todos"][0], values["todo"])
                case Sg.WIN_CLOSED:
                    break

        self.window.close()

    @staticmethod
    def _add_todo(new_todo):
        if not new_todo:
            return
        todos = functions.get_todos()
        todos.append(new_todo + "\n")
        functions.write_todos(todos)

    def _edit_todo(self, todo_to_edit, new_todo):
        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo + "\n"
        functions.write_todos(todos)
        self.window["todos"].update(values=todos)


if __name__ == "__main__":
    handler = TodoWindow()
    handler.process_user_input()
