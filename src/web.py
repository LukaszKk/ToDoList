import functions
import streamlit as st


class MainPage:
    def __init__(self):
        st.title("Todo App")
        st.subheader("This is todo app")
        st.write("This app is to increase productivity")
        self._write_todos()
        st.text_input(label="Add todo",
                      placeholder="Add new todo...",
                      on_change=self._add_todo, key="new_todo")

    def _write_todos(self):
        self.todos = functions.get_todos(r"src/todos.txt")
        for index, todo in enumerate(self.todos):
            checkbox = st.checkbox(todo, key=todo)
            if checkbox:
                self.todos.pop(index)
                functions.write_todos(self.todos, r"src/todos.txt")
                del st.session_state[todo]
                st.experimental_rerun()

    def _add_todo(self):
        todo = st.session_state["new_todo"] + "\n"
        self.todos.append(todo)
        functions.write_todos(self.todos, r"src/todos.txt")


if __name__ == "__main__":
    handler = MainPage()
