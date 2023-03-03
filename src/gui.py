import PySimpleGUI as Sg
from src import functions


if __name__ == "__main__":
    label = Sg.Text("Type in a todo")
    input_box = Sg.InputText(tooltip="Enter todo")
    add_button = Sg.Button("Add")

    window = Sg.Window("Todo app", layout=[[label], [input_box, add_button]])
    window.read()

    window.close()
